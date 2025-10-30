
pipeline {
    agent any
    
    environment {
        PROJECT = 'flask-ci-cd-demo'
        VENV_PATH = "${WORKSPACE}/venv"
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pytest -v test_app.py --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'main'
                expression { 
                    currentBuild.result == null || currentBuild.result == 'SUCCESS' 
                }
            }
            steps {
                echo 'Deploying to staging environment...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    # Stop any existing application
                    pkill -f "gunicorn" || true
                    # Start the application with gunicorn
                    nohup gunicorn -b 0.0.0.0:5000 app:app > app.log 2>&1 &
                    sleep 5
                '''
                sh '''
                    # Verify deployment
                    curl -f http://localhost:5000/health || exit 1
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The pipeline completed successfully.\\n\\nCheck console output at: ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'admin@example.com'}"
            )
        }
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "The pipeline failed.\\n\\nCheck console output at: ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL ?: 'admin@example.com'}"
            )
        }
    }
    
    triggers {
        pollSCM('H/5 * * * *')
    }
}
