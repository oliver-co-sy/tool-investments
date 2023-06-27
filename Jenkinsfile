pipeline {
    agent {
        docker {
            image 'python:3.11-slim-bookworm'
            args '-u root:root'
        }
    }

    parameters {
        string name: "SYMBOLS", description: "The stock symbols to query (separated by space)", trim: true
        string name: "TITLE", description: "The title of the Google Sheet", trim: true
        string name: "EMAIL", description: "The email address to share the report with", trim: true
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
                    sh 'cp $KEY_PATH .'
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

        stage("Run") {
            steps {
                sh "python3 stockreport.py -s ${SYMBOLS} -t ${TITLE} -e ${EMAIL}"
            }
        }
    }
}