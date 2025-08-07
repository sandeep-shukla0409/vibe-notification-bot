pipeline {
  agent any

  environment {
    TEAMS_WEBHOOK = credentials('teams-webhook-url') // store your Teams webhook in Jenkins Credentials
    DOCKER_IMAGE = 'flask-gist-app'
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/sandeep-shukla0409/vibe-coding.git'
      }
    }

    stage('Install & Test') {
      steps {
        sh '''
          pip install --no-cache-dir -r requirements.txt
          pytest --maxfail=1 --disable-warnings -q
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t $DOCKER_IMAGE ."
      }
    }
  }

  post {
    success {
      script {
        def payload = """
        {
          "@type": "MessageCard",
          "@context": "http://schema.org/extensions",
          "summary": "CI/CD Pipeline Success",
          "themeColor": "00FF00",
          "title": "✅ CI/CD succeeded for ${env.JOB_NAME} on ${env.BRANCH_NAME}",
          "text": "The pipeline completed successfully."
        }
        """
        sh "curl -H 'Content-Type: application/json' -d '${payload.trim()}' $TEAMS_WEBHOOK"
      }
    }
    failure {
      script {
        def payload = """
        {
          "@type": "MessageCard",
          "@context": "http://schema.org/extensions",
          "summary": "CI/CD Pipeline Failure",
          "themeColor": "FF0000",
          "title": "❌ CI/CD failed for ${env.JOB_NAME} on ${env.BRANCH_NAME}",
          "text": "The pipeline failed. Please check the logs."
        }
        """
        sh "curl -H 'Content-Type: application/json' -d '${payload.trim()}' $TEAMS_WEBHOOK"
      }