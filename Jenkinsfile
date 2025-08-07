pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vibe-notification-bot'
        TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'vibe-notification-bot'
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
                    docker stop ${CONTAINER_NAME}
                    docker rm ${CONTAINER_NAME}
                    docker run -d --name ${CONTAINER_NAME} -p 8080:8080 ${IMAGE_NAME}:${TAG}
                """
            }
        }
    }
}