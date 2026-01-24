
FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt update && \
    apt install -y python3 python3-pip python3-pytest python3-venv allure docker-compose && \
    apt clean

RUN usermod -aG root jenkins    

USER jenkins