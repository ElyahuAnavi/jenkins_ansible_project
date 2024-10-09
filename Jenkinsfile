pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs() // מנקה את תיקיית ה-Workspace
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python --version' // בדיקת גרסת Python
                bat 'python script.py' // הרצת הסקריפט
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
