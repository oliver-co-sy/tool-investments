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
                withDockerContainer('python:3.9.17-alpine3.18') {
                    sh "python3 -m venv .venv"
                    sh "source ./.venv/bin/activate"
                    sh "pip install -r requirements.txt"
                }
            }
        }
    }
}