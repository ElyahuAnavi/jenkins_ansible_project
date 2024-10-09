pipeline {
    agent any
    stages {
        stage('Run Python Script') {
            steps {
                // הגדרת python לפעולה בסביבת pipeline
                withPythonEnv('Python_3.12.6') {
                    sh 'python --version' // בדוק את גרסת Python
                    bat 'python script.py' // הרץ את סקריפט ה-Python
                }
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
