pipeline {
    agent { label 'slave01' }

    environment {
        DOCKER_HUB_IMAGE = "sathish1102/new-py1"
        TEST_SERVER = "172.31.9.228"
        DEPLOY_DIR = "/home/devopsadmin/app-deploy-dir"
        GIT_REPO = "https://github.com/Sathish-11/docker.git"
        DEPLOY_CONTAINER_NAME = "My-first-containe2211"
        DEPLOY_PORT_MAPPING = "8083:8000"
    }

    stages {
        stage('Clone Git Repo') {
            steps {
                git url: "${GIT_REPO}", branch: "main"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB_IMAGE .'
                sh 'docker images'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'a4cc6598-bede-4574-b8a4-bf19bea857f0', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push $DOCKER_HUB_IMAGE
                    '''
                }
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                script {
                    def removeContainerCmd = "docker rm -f ${DEPLOY_CONTAINER_NAME} || true"
                    def runContainerCmd = "docker run -itd --name ${DEPLOY_CONTAINER_NAME} -p ${DEPLOY_PORT_MAPPING} ${DOCKER_HUB_IMAGE}"

                    sshagent(['Deploy_Server']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no devopsadmin@${TEST_SERVER} '${removeContainerCmd}'
                            ssh -o StrictHostKeyChecking=no devopsadmin@${TEST_SERVER} '${runContainerCmd}'
                        """
                    }
                }
            }
        }
    }
}

