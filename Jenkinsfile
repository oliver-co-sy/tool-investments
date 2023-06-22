pipeline {
    agent {
        docker {
            image 'python:3.9-bookworm'
            // args '-u root:root'
            args '--tmpfs /.config'
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
                sh "pip3 install -r requirements.txt"
            }
        }
    }
}