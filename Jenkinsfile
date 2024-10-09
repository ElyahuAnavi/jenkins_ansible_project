pipeline {
    agent any
    tools {
        python 'Python_3.12.6' // יש להשתמש בשם התקנת Python כפי שהוגדר ב-Jenkins
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python --version' // בדיקה ש-Python עובד
                bat 'python script.py' // הפעלת הסקריפט
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
