pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('List Files') {
            steps {
                bat 'dir' // מציג את כל הקבצים בתיקיית ה-Workspace
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                // קריאה ל-Playbook ושימוש בקובץ inventory
                ansiblePlaybook playbook: 'ansible_playbook.yml', inventory: 'inventory'
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
