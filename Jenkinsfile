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
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                sh 'docker compose up -d db prestashop'
            }
        }

        stage('Run Tests') {
            steps {
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
                            echo "Copying allure results from container..."
                            sh "docker cp ${testContainer}:/app/allure-results/. ./allure-results/ || true"
                            sh "docker rm -f ${testContainer} || true"
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