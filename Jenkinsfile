pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage("Cleanup") {
            steps {
                cleanWs()
            }
        }
        stage("Checkout") {
            steps {
                checkout scm
                sh 'echo "Workspace contents after checkout:" && ls -R' // Debug: List all files and directories
            }
        }
        stage("Build") {
            agent {
                docker {
                    image 'python:3.11-alpine'
                    args '-u root'
                }
            }
            steps {
               sh '''
                # List files in the current workspace
                ls -l
                
                # Display Python and pip versions
                python --version
                pip --version
                
                # Install dependencies (assuming requirements.txt exists)
                pip install -r requirements.txt
                
                # Run the Flask application build or initialization commands
                export FLASK_APP=app.py
                flask --help # Check Flask is correctly installed
                ls -l
            '''
            }
        }
    }
}
