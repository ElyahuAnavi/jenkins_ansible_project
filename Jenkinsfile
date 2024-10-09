pipeline {
    agent any
    tools {
        'PythonInstallation' 'Python_3.12.6' // שם הכלי בהתאם ל-ShiningPanda
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python --version' // וידוא שה-Python עובד
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
