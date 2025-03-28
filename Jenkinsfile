pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'sqa_195c69cd5a4b586bee1a303d97df5f8b52e28b41' // Replace with your actual token
        TARGET_URL = 'http://localhost:8080' // Replace with your target web app URL
    }

    stages {
        stage('Checkout Code') {
            steps {
                // For demo purposes, we're simply echoing a message.
                // In a real scenario, checkout your repo here.
                echo 'Checking out code...'
            }
        }

        stage('Static Code Analysis (SonarQube)') {
            steps {
                script {
                    echo 'Running SonarQube analysis...'
                    // Uncomment and update the following commands if you have a Maven project:
                    // bat 'mvn sonar:sonar -Dsonar.projectKey=sample-project -Dsonar.host.url=%SONARQUBE_URL% -Dsonar.login=%SONARQUBE_TOKEN%'
                }
            }
        }

        stage('Build and Containerize') {
            steps {
                script {
                    echo 'Building application and creating Docker image...'
                    // Uncomment and update for your application:
                    // bat 'mvn clean package'
                    // bat 'docker build -t sample-app:latest .'
                }
            }
        }

        stage('Dynamic Security Testing (OWASP ZAP)') {
            steps {
                script {
                    echo 'Triggering dynamic security scan with OWASP ZAP...'
                    // Use bat commands on Windows; environment variables use %VARIABLE_NAME%
                    bat 'curl -X POST "http://localhost:8081/JSON/ascan/action/scan/?url=%TARGET_URL%&recurse=true"'
                    // Pause for 30 seconds to allow the scan to initiate
                    bat 'timeout /T 30'
                    // Retrieve scan alerts from ZAP
                    bat 'curl "http://localhost:8081/JSON/alert/view/alerts/"'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying Docker container...'
                    // Uncomment and update if you have a Docker image to run:
                    // bat 'docker run -d -p 80:80 sample-app:latest'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution finished."
        }
        failure {
            echo "Pipeline failed. Please check the logs for details."
        }
    }
}
