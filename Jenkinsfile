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
                sh 'echo "Workspace contents after checkout:" && ls -R'
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

                    echo "Listing files in the container's working directory..."
                    ls -l
                    
                    echo "Checking Python and pip versions..."
                    python --version
                    pip --version

                    echo "Checking for requirements.txt in the container..."
                    if [[ ! -f "requirements.txt" ]]; then
                        echo "Error: requirements.txt not found in $(pwd)"
                        echo "Listing all files in the current directory:"
                        ls -la
                        exit 1
                    fi

                    echo "Installing dependencies from requirements.txt..."
                    pip install -r requirements.txt

                    echo "Setting up Flask application..."
                    if [[ ! -f "app.py" ]]; then
                        echo "Error: app.py not found!"
                        exit 1
                    fi
                    export FLASK_APP=app.py
                    flask --help
                '''
            }
        }
    }
}
