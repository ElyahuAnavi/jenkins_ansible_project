pipeline {
    agent any
    stages {
        stage('Check PATH') {
            steps {
                bat 'echo %PATH%' // מציג את משתנה ה-PATH הנוכחי
            }
        }
        stage('Run Python Script') {
            steps {
                bat 'python --version' // בדוק את גרסת Python
            }
        }
    }
}
