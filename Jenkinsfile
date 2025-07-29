pipeline {
    agent any
    stages{
        stage('git cloned'){
            steps{
                git url:'https://github.com/Sathish-11/docker.git', branch: "master"
              
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t sathish1102/newimg-py1:v1 .'
                    sh 'docker images'
                }
            }
        }
      }
}
