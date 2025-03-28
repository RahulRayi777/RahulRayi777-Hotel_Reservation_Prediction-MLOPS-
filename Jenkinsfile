pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-new-447207"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/RahulRayi777/RahulRayi777-Hotel_Reservation_Prediction-MLOPS-.git']])

                }
            }
        }
    }
}
       