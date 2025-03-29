pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-new-447207"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        IMAGE_NAME = "hotel-reservation"
    }

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps {
                script {
                    echo '📥 Cloning Github repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/master']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/RahulRayi777/RahulRayi777-Hotel_Reservation_Prediction-MLOPS-'
                        ]]
                    )
                }
            }
        }

        stage('Setting up Virtual Environment & Installing dependencies') {
            steps {
                script {
                    echo '⚙️ Setting up Virtual Environment and Installing dependencies...'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                }
            }
        }

        stage('Run Training Pipeline') {
            steps {
                script {
                    echo '🚀 Running Training Pipeline...'
                    sh '''
                        . ${VENV_DIR}/bin/activate
                        python pipeline/training_pipeline.py
                    '''
                }
            }
        }

        stage('Building and Pushing Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo '🐳 Building and Pushing Docker Image to GCR...'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}
                            gcloud auth configure-docker --quiet
                            
                            docker build -t gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:latest .
                            docker push gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo '🚀 Deploying to Google Cloud Run...'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}

                            gcloud run deploy ${IMAGE_NAME} \
                                --image=gcr.io/${GCP_PROJECT}/${IMAGE_NAME}:latest \
                                --platform=managed \
                                --region=us-central1 \
                                --allow-unauthenticated
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
