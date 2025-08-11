pipeline {
    agent any

    environment {
        IMAGE_NAME = 'vibe-notification-bot'
        DOCKER_REPO = '' // Replace with your Docker registry/repo
        CONTAINER_PORT = '8080'
    }

    stages {
        stage('Build Dev Image') {
            steps {
                echo "🔧 Building DEV image..."
                bat """
                    docker build -t %IMAGE_NAME%:dev .
                """
            }
        }

        stage('Run Tests in Dev Container') {
            steps {
                echo "🧪 Running tests inside container..."
                bat """
                    docker run --rm %IMAGE_NAME%:dev pytest test/ --cache-clear
                """
            }
        }

        stage('Push Dev Image') {
            when { branch 'develop' }
            steps {
                echo "📦 Tagging and pushing DEV image..."
                bat """
                    docker tag %IMAGE_NAME%:dev %DOCKER_REPO%/%IMAGE_NAME%:dev
                    docker push %DOCKER_REPO%/%IMAGE_NAME%:dev
                """
            }
        }

        stage('Promote Dev to Test') {
            when { branch 'test' }
            steps {
                echo "🚀 Promoting DEV to TEST..."
                bat """
                    docker pull %DOCKER_REPO%/%IMAGE_NAME%:dev
                    docker tag %DOCKER_REPO%/%IMAGE_NAME%:dev %DOCKER_REPO%/%IMAGE_NAME%:test
                    docker push %DOCKER_REPO%/%IMAGE_NAME%:test
                """
            }
        }

        stage('Promote Test to Prod') {
            when { branch 'main' }
            steps {
                echo "🚀 Promoting TEST to PROD..."
                bat """
                    docker pull %DOCKER_REPO%/%IMAGE_NAME%:test
                    docker tag %DOCKER_REPO%/%IMAGE_NAME%:test %DOCKER_REPO%/%IMAGE_NAME%:prod
                    docker push %DOCKER_REPO%/%IMAGE_NAME%:prod
                """
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    def envTag = (env.BRANCH_NAME == 'main') ? 'prod' :
                                 (env.BRANCH_NAME == 'test') ? 'test' : 'dev'
                    def containerName = "${IMAGE_NAME}-${envTag}"
                    def hostPort = (envTag == 'prod') ? '9292' :
                                   (envTag == 'test') ? '9191' : '9090'

                    echo "🚀 Deploying ${envTag.toUpperCase()} container on port ${hostPort}..."

                    bat """
                        docker rm -f ${containerName}
                        docker run -d --name ${containerName} -p ${hostPort}:${CONTAINER_PORT} ${DOCKER_REPO}/${IMAGE_NAME}:${envTag}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully."
        }
        failure {
            echo "❌ Pipeline failed. Check logs for details."
        }
    }
}