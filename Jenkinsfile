pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vibe-notification-bot'
        TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'vibe-notification-bot'
        CONTAINER_PORT=8080
        HOST_PORT=9090
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Run Tests') {
            steps {
                bat "docker run --rm ${IMAGE_NAME}:${TAG} pytest test/"
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                    docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:${TAG}
                """
            }
        }
    }
}