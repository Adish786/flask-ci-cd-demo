pipeline {
    agent any

    environment {
        APP_NAME = "flask-ci-cd-demo"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Adish786/flask-ci-cd-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh '''
                echo "Deploying ${APP_NAME} to staging environment..."
                # Example deploy (you can replace this with your actual deploy step)
                nohup python app.py &
                '''
            }
        }
    }

    post {
        success {
            mail to: 'Adishansari786@gmail.com',
                 subject: "✅ Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build ${env.BUILD_URL} succeeded."
        }
        failure {
            mail to: 'Adishansari786@gmail.com',
                 subject: "❌ Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Check the logs at ${env.BUILD_URL}"
        }
    }
}
