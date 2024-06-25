pipeline {
    agent { label 'linux' }
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    
    environment {
        SERVICE_NAME = 'your_service_name'  // Replace with your actual service name
        VERSION = '1.0.0'                   // Replace with your desired version
        BUILD_NUMBER = env.BUILD_NUMBER      // Jenkins-provided build number
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Alert Management Building Process Started"
                echo "Service Name: ${SERVICE_NAME}"
                echo "Version: ${VERSION}"
                echo "Build Number: ${BUILD_NUMBER}"
                
                script {
                    // Execute Docker build command
                    sh "docker build -t ${SERVICE_NAME}:${VERSION}-${BUILD_NUMBER} --label version=${VERSION}-${BUILD_NUMBER} ."
                }
                
                echo "Alert Management Building Process End"
            }
        }
        
        stage('Scan') {
            steps {
                script {
                    // Execute Trivy vulnerability scan
                    sh "trivy ${SERVICE_NAME}:${VERSION}-${BUILD_NUMBER}"
                }
            }
        }
    }
}
