pipeline{
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = credentials('telegram_bot_token')
        TELEGRAM_CHAT_ID = credentials('telegram_chat_id')
        PROJECT_SUB_DIR = 'web_Scraper'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment with UV...'
                    sh 'curl -LsSf https://astral.sh/uv/install.sh | sh'
                    // Add the installation path to the PATH environment variable for subsequent steps
                    sh 'export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"'

                    dir("${PROJECT_SUB_DIR}") {
                        sh '''
                            echo "Current directory: $(pwd)"
                            echo "Path: $PATH"

                            ls -la $HOME/.local/bin/uv
                            echo 'Installing dependencies...'
                            export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

                            uv sync
                            echo "Dependencies installed."
                        '''
                    }
                }

            }
        }

        stage("Deploy") {
            steps {
                echo 'Starting the deployment process...'
                script{
                    dir("${PROJECT_SUB_DIR}") {
                        echo "Deploying the build number ${env.BUILD_NUMBER}"
                        sh 'chmod 755 ./scripts/deploy.sh'

                        sh "./scripts/deploy.sh deploy ${env.BUILD_NUMBER} "
                        echo "Deployment completed."
                    }
                }
                // Add deployment steps here if needed
            }
        }

        stage('Run the scraper') {
            steps {
                script {
                    dir("${PROJECT_SUB_DIR}") {
                        sh '''
                            echo "Current directory: $(pwd)"
                            echo "Path: $PATH"

                            echo 'Running the web scraper...'
                            export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

                            uv run main.py
                            echo "Web scraper executed."
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            script {    
            dir("${PROJECT_SUB_DIR}") {
                echo 'Pipeline failed. Sending notification...'
                sh '''
                    curl -s -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage -d chat_id=$TELEGRAM_CHAT_ID -d text="Jenkins Pipeline Failed. Please check the Jenkins console for details."
                '''
                 echo "Initiating the rollback for build ${env.BUILD_NUMBER}"
                sh 'chmod 755 ./scripts/deploy.sh'

                sh "./scripts/deploy.sh rollback"
                echo "Rollback completed."
            }
        }
      }
    }
}