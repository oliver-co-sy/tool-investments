pipeline {
    agent {
        docker {
            image 'python:3.11-slim-bookworm'
            args '-u root:root'
        }
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python3 -m venv .venv"
                sh ". ./.venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }
    }
}