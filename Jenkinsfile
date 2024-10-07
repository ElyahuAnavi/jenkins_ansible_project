pipeline {
    agent any
    stages {
        stage('Run Batch Script') {
            steps {
                script {
                    bat 'batch_script.bat'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
