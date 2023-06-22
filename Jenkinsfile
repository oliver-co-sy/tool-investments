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
                withDockerContainer('python:3.9-bookworm') {
                    // sh "python3 -m venv .venv"
                    // sh "source ./.venv/bin/activate"
                    sh "sudo pip3 install -r requirements.txt"
                }
            }
        }
    }
}