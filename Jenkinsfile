pipeline {
    agent any
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Select the deployment target for the Student System')
    }
    stages {
        stage('Checkout') {
            steps {
                // Replace with your actual GitHub URL
                git branch: 'main', url: 'https://github.com/sureshkrishnak76-jpg/student-parameter-pipeline.git'
            }
        }
        stage('Show Parameter') {
            steps {
                echo "Target deployment environment: ${params.ENVIRONMENT}"
            }
        }
        stage('Build for Environment') {
            steps {
                echo "Configuring Student Management System databases for the ${params.ENVIRONMENT} environment..."
            }
        }
    }
}
