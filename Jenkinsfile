pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your code from your GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/khadijairfan2345/task1.git']]])
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install Python and required dependencies
                sh 'pip install pytest'  // If you have a requirements file
            }
        }

        stage('Run Tests') {
            steps {
                // Run your test cases using pytest
                sh 'python square_test.py'
            }
        }
    }
}
