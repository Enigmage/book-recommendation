pipeline {
    agent any

    environment {
        // Define any environment variables you need
        PYTHON_VERSION = "3.12"
        APP_NAME = "book-recommendation"
        DOCKER_IMAGE = "2023sl93054/${APP_NAME}:latest"
        SONAR_HOST_URL = "http://3.231.129.5:9000"
        SONAR_PROJECT_KEY = "book-recommendation"
        SONAR_LOGIN = credentials("86ebb9e4-b848-4ab5-9957-de0eb2a5291d")
    }

    stages {
        stage("Checkout") {
            steps {
                // Checkout the code from Git
                git branch: "main", url: "https://github.com/Enigmage/book-recommendation.git"
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    // Build Docker image
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                    """
                }
            }
        }

        stage("SonarQube Analysis") {
            steps {
                script {
                    // Run SonarQube scanner
                    def scannerHome = tool name: "SonarQube", type: "hudson.plugins.sonar.SonarRunnerInstallation"
                    withSonarQubeEnv("SonarQube") {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=${SONAR_HOST_URL} \
                            -Dsonar.login=${SONAR_LOGIN} \
                            -Dsonar.python.version=${PYTHON_VERSION}
                        """
                    }
                }
            }
        }

        stage("Quality Gate") {
            steps {
                script {
                    // Check the quality gate result
                    timeout(time: 5, unit: "MINUTES") {
                        waitForQualityGate abortPipeline: false
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
