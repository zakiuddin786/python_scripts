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
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}