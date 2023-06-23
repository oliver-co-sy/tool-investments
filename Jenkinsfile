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

        stage("Copy Key") {
            steps {
                withCredentials([file(credentialsId: 'GoogleSheetsKey', variable: 'KEY_PATH')]) {
                    sh "cp ${KEY_PATH} ."
                }
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python3 -m venv .venv"
                sh ". ./.venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Execute") {
            steps {
                sh "python3 stockreport.py -s TD.TO RY.TO BMO.TO -t stock_today-062223 -e oliver.co.sy@gmail.com"
            }
        }
    }
}