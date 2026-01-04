#!/bin/bash

set -e

ACTION=$1
BUILD_NUMBER=$2
DEPLOY_DIR="deployments"
CURRENT_LINK="$DEPLOY_DIR/current"

mkdir -p "$DEPLOY_DIR"

update_link() {
    target_link=$1
    echo "Updating current deployment link to $target_link"

    ln -sfn $target_link "$CURRENT_LINK"
}

if [ "$ACTION" == "deploy" ]; then
    [[ -z "$BUILD_NUMBER" ]] && { echo "Build number is required for deployment."; exit 1; }

    NEW_DEPLOY_DIR="$DEPLOY_DIR/build_$BUILD_NUMBER"
    echo "Deploying new version to $NEW_DEPLOY_DIR"

    mkdir -p "$NEW_DEPLOY_DIR"
    rsync -a --exclude={'.git',"deployments",".venv", "__pycache__"} ./ "$NEW_DEPLOY_DIR/"

    update_link "$NEW_DEPLOY_DIR"
    echo "Deployment completed successfully."

elif [ "$ACTION" == "rollback" ]; then
    echo "Rolling back to previous deployment."
    if [ -L "$CURRENT_LINK" ]; then
        CURRENT_TARGET=$(readlink "$CURRENT_LINK")
        echo "Current deployment is $CURRENT_TARGET"

        PREV_DEPLOY_DIR=$(ls -td $DEPLOY_DIR/build_* | grep -v "$CURRENT_TARGET" | head -n 1)

        if [ -z "$PREV_DEPLOY_DIR" ]; then
            echo "No previous deployment found to rollback to."
            exit 1
        fi
        echo "Previous deployment found: $PREV_DEPLOY_DIR initiating rollback."

        update_link "$PREV_DEPLOY_DIR"
        echo "Rolled back to previous deployment: $PREV_DEPLOY_DIR"
    else
        echo "No current deployment found to rollback from."
        exit 1
    fi
else
    echo "Invalid action. Use 'deploy' or 'rollback'."
    exit 1
fi