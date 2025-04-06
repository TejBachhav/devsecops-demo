pipeline {
    agent any

    // Define global environment variables
    environment {
        SONARQUBE_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'sqa_195c69cd5a4b586bee1a303d97df5f8b52e28b41' // Replace with your token
        TARGET_URL = 'http://your-web-app-url' // Replace with your target web app URL
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Since this is a demo, we're simply echoing a message.
                // In a real scenario, you'd checkout from a repo.
                echo 'Checking out code...'
            }
        }

        stage('Static Code Analysis (SonarQube)') {
            steps {
                script {
                    echo 'Running SonarQube analysis...'
                    // Uncomment the following if you have a Maven project:
                    // sh """
                    //     mvn sonar:sonar \
                    //     -Dsonar.projectKey=sample-project \
                    //     -Dsonar.host.url=${SONARQUBE_URL} \
                    //     -Dsonar.login=${SONARQUBE_TOKEN}
                    // """
                }
            }
        }

        stage('Build and Containerize') {
            steps {
                script {
                    echo 'Building application and creating Docker image...'
                    // Uncomment and update the commands for your application:
                    sh 'mvn clean package'
                    sh 'docker build -t sample-app:latest .'
                }
            }
        }

        stage('Dynamic Security Testing (OWASP ZAP)') {
            steps {
                script {
                    echo 'Triggering dynamic security scan with OWASP ZAP...'
                    // Replace http://localhost:8081 with your ZAP host/port if different:
                    sh """
                        curl -X POST "http://localhost:8082/JSON/ascan/action/scan/?url=${TARGET_URL}&recurse=true"
                    """
                    sleep(time: 30, unit: 'SECONDS')
                    sh """
                        curl "http://localhost:8082/JSON/alert/view/alerts/"
                    """
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying Docker container...'
                    // Uncomment and update if you have a Docker image to run:
                    // sh 'docker run -d -p 80:80 sample-app:latest'
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
