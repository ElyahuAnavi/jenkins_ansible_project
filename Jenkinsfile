pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs() // לנקות את ה-Workspace
            }
        }
        stage('Run Python Script') {
            steps {
                // הפעלת הסקריפט באמצעות פקודת Batch המתאימה ל-Windows
                bat 'python --version'
                bat 'python script.py'
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
