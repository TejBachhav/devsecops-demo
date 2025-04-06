pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'your_sonarqube_token' // Replace with your token
        TARGET_URL = 'http://your-web-app-url' // Replace with your target web app URL
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
                    // Uncomment and update the commands for your application:
                    // sh 'mvn clean package'
                    // sh 'docker build -t sample-app:latest .'
                }
            }
        }

        stage('Dynamic Security Testing (OWASP ZAP)') {
            steps {
                script {
                    echo 'Triggering dynamic security scan with OWASP ZAP...'
                    // Replace http://localhost:8081 with your ZAP host/port if different:
                    sh """
                        curl -X POST "http://localhost:8081/JSON/ascan/action/scan/?url=${TARGET_URL}&recurse=true"
                    """
                    sleep(time: 30, unit: 'SECONDS')
                    sh """
                        curl "http://localhost:8081/JSON/alert/view/alerts/"
                    """
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
