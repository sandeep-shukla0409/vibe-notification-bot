pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vibe-notification-bot'
        TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'vibe-notification-bot'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME} pytest test/"
            }
        }

        stage('Deploy Container') {
            steps {
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 8080:8080 ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "✅ App deployed locally. Access it at http://localhost:5000"
        }
        failure {
            echo "❌ Something went wrong. Check the logs."
        }
    }
}