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
                    sh "pip install -r requirements.txt"
                }
            }
        }
    }
}