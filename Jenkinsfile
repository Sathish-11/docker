pipeline {
    agent { label 'slave01' }
    environment {
        DOCKER_HUB_IMAGE = "sathish1102/newimg-py1"
        TEST_SERVER = "172.31.15.47"
        DEPLOY_DIR = "/home/devopsadmin/app-deploy-dir"
        GIT_REPO = "https://github.com/Sathish-11/docker.git"
    }
    stages{
        stage('git cloned'){
            steps{
                git url:'$GIT_REPO', branch: "main"
              
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t $DOCKER_HUB_IMAGE .'
                    sh 'docker images'
                }
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB_IMAGE .'
                withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push $DOCKER_HUB_IMAGE
                    '''
                }
            }
        }
        stage('Deploy to Test Server using Docker Compose') {
            steps{
                sshagent(['Deploy_Server']){
                    withCredentials([usernamePassword(credentialsId: 'a4cc6598-bede-4574-b8a4-bf19bea857f0', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                        sh 'docker build -t $Docker_username .'
                    }
                }
            } 
      }
}
