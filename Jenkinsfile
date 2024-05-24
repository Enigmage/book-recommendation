pipeline {
    agent any

    environment {
        // Define any environment variables you need
        PYTHON_VERSION = '3.12'
        APP_NAME = 'book-recommendation'
        DOCKER_IMAGE = "2023sl93054/${APP_NAME}:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git
                git branch: 'main', url: 'https://github.com/Enigmage/book-recommendation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh '''
                        docker build -t ${DOCKER_IMAGE} .
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up any temporary files, etc.
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
