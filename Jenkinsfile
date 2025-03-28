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
                echo 'Checking out code...'
                // In a real scenario, you would check out your repo.
            }
        }

        stage('Static Code Analysis (SonarQube)') {
            steps {
                script {
                    echo 'Running SonarQube analysis...'
                    // Uncomment if you have a Maven project:
                    // bat 'mvn sonar:sonar -Dsonar.projectKey=sample-project -Dsonar.host.url=%SONARQUBE_URL% -Dsonar.login=%SONARQUBE_TOKEN%'
                }
            }
        }

        stage('Build and Containerize') {
            steps {
                script {
                    echo 'Building application and creating Docker image...'
                    // Uncomment and update if you have build commands:
                    // bat 'mvn clean package'
                    // bat 'docker build -t sample-app:latest .'
                }
            }
        }

        stage('Dynamic Security Testing (OWASP ZAP)') {
            steps {
                script {
                    echo 'Triggering dynamic security scan with OWASP ZAP...'
                    // Ensure your OWASP ZAP container is running and mapped to port 8081
                    bat 'curl -X POST "http://localhost:8081/JSON/ascan/action/scan/?url=%TARGET_URL%&recurse=true"'
                    // Wait for 30 seconds using ping for delay
                    bat 'ping -n 31 127.0.0.1 >nul'
                    bat 'curl "http://localhost:8081/JSON/alert/view/alerts/"'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying Docker container...'
                    // Uncomment and update if you have a Docker run command:
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
