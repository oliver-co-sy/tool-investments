pipeline {
    agent {
        docker {
            image 'python:3.11-slim-bookworm'
            args '-u root:root'
        }
    }

    parameters {
        choice name: "JOB", choices: ["Generate Stock Report", "Update Reference Stocks"], description: "Determines the action that will be performed" 
        string name: "SYMBOLS", description: "The stock symbols to query (separated by space)", trim: true
        string name: "TITLE", description: "The title of the Google Sheet", trim: true
        string name: "WORKSHEET", description: "The Google Sheet worksheet title (Only applies to the Update Reference Stocks job)", trim: true
        string name: "EMAIL", description: "The email address to share the report with (Only applies to the Generate Stock Report job)", trim: true
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

        stage("Generate Stock Report") {
            when {
                environment name: "JOB", value: "Generate Stock Report", ignoreCase: true
            }
            steps {
                sh "python3 stockreport.py -s ${params.SYMBOLS} -t ${params.TITLE} -e ${params.EMAIL}"
            }
        }

        stage("Update Reference Stocks") {
            when {
                environment name: "JOB", value: "Update Reference Stocks", ignoreCase: true
            }
            steps {
                sh "python3 updatereferencedata.py -s ${params.SYMBOLS} -t ${params.TITLE} -w ${params.WORKSHEET}"
            }
        }
    }
}