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
                    set -e

                    echo "Listing files in the workspace..."
                    ls -l

                    echo "Checking Python and pip versions..."
                    python --version
                    pip --version

                    echo "Installing dependencies from requirements.txt..."
                    if [[ ! -f "requirements.txt" ]]; then
                        echo "Error: requirements.txt not found!"
                        exit 1
                    fi
                    pip install -r requirements.txt

                    echo "Setting up Flask application..."
                    if [[ ! -f "app.py" ]]; then
                        echo "Error: app.py not found!"
                        exit 1
                    fi
                    export FLASK_APP=app.py
                    flask --help

                    echo "Listing files after setup..."
                    ls -l
                '''
            }
        }
    }
}
