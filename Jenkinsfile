// pipeline {
//     agent any

//     environment {
//         SONARQUBE_URL = 'http://localhost:9000'
//         SONARQUBE_TOKEN = 'sqa_314c05b42c628e90fd6cd6566dc74397e0e8ae44' // Replace with your token
//         TARGET_URL = 'https://your-tube2.netlify.app/' // Replace with your target web app URL
//     }

//     stages {
//         stage('Checkout Code') {
//             steps {
//                 echo 'Checking out code...'
//                 // In a real scenario, you would check out your repo.
//             }
//         }

//         stage('Static Code Analysis (SonarQube)') {
//             steps {
//                 script {
//                     echo 'Running SonarQube analysis...'
//                     // Uncomment if you have a Maven project:
//                     // bat 'mvn sonar:sonar -Dsonar.projectKey=sample-project -Dsonar.host.url=%SONARQUBE_URL% -Dsonar.login=%SONARQUBE_TOKEN%'
//                 }
//             }
//         }

//         stage('Build and Containerize') {
//             steps {
//                 script {
//                     echo 'Building application and creating Docker image...'
//                     // Uncomment and update the commands for your application:
//                     // sh 'mvn clean package'
//                     // sh 'docker build -t sample-app:latest .'
//                 }
//             }
//         }

//         stage('Dynamic Security Testing (OWASP ZAP)') {
//             steps {
//                 script {
//                     echo 'Triggering dynamic security scan with OWASP ZAP...'
//                     // Replace http://localhost:8081 with your ZAP host/port if different:
//                     sh """
//                         curl -X POST "http://localhost:8081/JSON/ascan/action/scan/?url=${TARGET_URL}&recurse=true"
//                     """
//                     sleep(time: 30, unit: 'SECONDS')
//                     sh """
//                         curl "http://localhost:8081/JSON/alert/view/alerts/"
//                     """
//                 }
//             }
//         }

//         stage('Deploy to Production') {
//             steps {
//                 script {
//                     echo 'Deploying Docker container...'
//                     // Uncomment and update if you have a Docker run command:
//                     // bat 'docker run -d -p 80:80 sample-app:latest'
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             echo "Pipeline execution finished."
//         }
//         failure {
//             echo "Pipeline failed. Please check the logs for details."
//         }
//     }
// }


pipeline {
    agent any

    environment {
        SONARQUBE_URL = 'http://localhost:9000'
        SONARQUBE_TOKEN = 'sqa_314c05b42c628e90fd6cd6566dc74397e0e8ae44' // Replace with your token
        TARGET_URL = 'https://your-tube2.netlify.app/' // Replace with your deployed app URL
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '🔄 Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Skipping dependency installation — no package.json found.'
            }
        }

        stage('Static Code Analysis (SonarQube)') {
            steps {
                script {
                    echo '🔍 Running SonarQube analysis...'
                    // Example command for a Maven project on Windows
                    // bat 'mvn sonar:sonar -Dsonar.projectKey=your-key -Dsonar.host.url=%SONARQUBE_URL% -Dsonar.login=%SONARQUBE_TOKEN%'
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    echo '🏗️ Building the application...'
                    // Add your actual build command below (e.g., Maven, Gradle, Python, etc.)
                    // bat 'mvn clean package'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '🐳 Building Docker image...'
                    // Example (customize tag and Dockerfile if needed)
                    // bat 'docker build -t my-app:latest .'
                }
            }
        }

        stage('Dynamic Security Testing (OWASP ZAP)') {
            steps {
                script {
                    echo '🛡️ Running OWASP ZAP scan...'
                    bat """
                        curl -X POST "http://localhost:8092/JSON/ascan/action/scan/?url=%TARGET_URL%&recurse=true"
                    """
                    sleep(time: 30, unit: 'SECONDS')
                    bat """
                        curl "http://localhost:8092/JSON/alert/view/alerts/"
                    """
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo '🚀 Deploying the Docker container...'
                    // Example (customize ports and image name)
                    // bat 'docker run -d -p 80:80 my-app:latest'
                }
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline execution completed."
        }
        failure {
            echo "❌ Pipeline failed. Please check logs."
        }
    }
}
