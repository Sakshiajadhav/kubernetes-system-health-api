#!/bin/bash

IMAGE_NAME="sakshiajadhav/system-health-api"
TAG=${1:-latest}

docker build -t ${IMAGE_NAME}:${TAG} .
echo "Built image: ${IMAGE_NAME}:${TAG}"