pipeline {
    agent any

    parameters {
        string(name: 'HUB_EXECUTOR', defaultValue: 'nginx', description: 'Адрес Selenoid (имя сервиса в сети)')
        string(name: 'APP_URL', defaultValue: 'http://prestashop', description: 'URL приложения')
        choice(name: 'BROWSER_NAME', choices: ['ch', 'ff', 'edge'], description: 'Браузер')
        string(name: 'BROWSER_VERSION', defaultValue: '128.0', description: 'Версия браузера')
        string(name: 'THREADS', defaultValue: '1', description: 'Количество потоков (нужен плагин pytest-xdist)')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Клонирование репозитория...'
                checkout scm
            }
        }

    stage('Linting') {
        steps {
            script {
            echo "Проверка линтером Ruff..."
                try {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/python3 -m pip install ruff
                    ./venv/bin/python3 -m ruff check .
                '''
                } finally {
                echo "Очистка виртуального окружения..."
                sh 'rm -rf venv'
                }
            }
        }
    }

        stage('Prepare Environment') {
            steps {
                echo 'Запуск сервисов через Docker Compose...'
                sh 'docker compose down -v || true'
                sh 'docker compose up -d db prestashop'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Запуск тестов из контейнера через Docker Compose...'
                withCredentials([usernamePassword(
                    credentialsId: 'PRESTASHOP_ADMIN_CREDS', 
                    usernameVariable: 'EXTRACTED_EMAIL', 
                    passwordVariable: 'EXTRACTED_PASS'
                )]) {
                    script {
                        sh 'mkdir -p allure-results'
                        def testContainer = "tests_runner_${BUILD_NUMBER}"
                        
                        try {
                            sh """
                            docker compose run --name ${testContainer} \
                                -e HUB_EXECUTOR=${params.HUB_EXECUTOR} \
                                -e APP_URL=${params.APP_URL} \
                                -e BROWSER_NAME=${params.BROWSER_NAME} \
                                -e BROWSER_VERSION=${params.BROWSER_VERSION} \
                                -e ADMIN_EMAIL=${EXTRACTED_EMAIL} \
                                -e ADMIN_PASSWORD=${EXTRACTED_PASS} \
                                tests /bin/sh -c "
                                    echo 'Waiting for PrestaShop...' && sleep 240;
                                    echo 'Cleaning install folder...' && rm -rf /var/www/html_site/install;
                                    pytest -n ${params.THREADS} \
                                    --browser ${params.BROWSER_NAME} \
                                    --url ${params.APP_URL} \
                                    --browser_version ${params.BROWSER_VERSION} \
                                    --executor ${params.HUB_EXECUTOR} \
                                    --alluredir=/app/allure-results
                                "
                            """
                        } finally {
                            echo "Копирование allure results из контейнера..."
                            sh "docker cp ${testContainer}:/app/allure-results/. ./allure-results/ || true"
                            echo "Удаляем контейнер с тестами, останавливаем сервисы..."
                            sh "docker rm -f ${testContainer} || true"
                            sh "docker compose down -v || true"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, 
                   jdk: '', 
                   results: [[path: 'allure-results']]
        }
    }
}