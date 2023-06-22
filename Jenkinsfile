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
                withDockerContainer('python:3.8-alpine') {
                    sh "python3 -m venv .venv"
                    sh "source ./.venv/bin/activate"
                    sh "pip3 install -r requirements.txt"
                }
            }
        }
    }
}