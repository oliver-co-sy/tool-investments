pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Install Dependencies") {
            steps {
                withDockerContainer('python:3.7-alpine') {
                    sh "python3 -m venv .venv"
                    sh "source ./.venv/bin/activate"
                    sh "sudo -H pip install -r requirements.txt"
                }
            }
        }
    }
}