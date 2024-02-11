pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Apply Migrations') {
            steps {
                sh 'python manage.py migrate'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'testing the appliaction...'
            }
        }
        stage('Start Server') {
            steps {
                sh 'python manage.py runserver'
            }
        }
    }
}
