pipeline {
    agent any
    stages {
        stage('List Files') {
            steps {
                bat 'dir' // מציג את כל הקבצים בתיקיית ה-Workspace
            }
        }
        stage('Run Python Script') {
            steps {
                bat 'python script.py' // מריץ את הסקריפט
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
