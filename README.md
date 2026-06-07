# Kubernetes System Health API

A production-style DevOps project that deploys a Python Flask system health API using Docker, Kubernetes, GitHub Actions, ConfigMaps, health probes, resource limits, shell scripts, and automated tests.

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-black)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5)](https://kubernetes.io/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)



## Tech Stack

- Python 3.10
- Flask
- Gunicorn
- Docker
- Kubernetes
- GitHub Actions
- Bash
- pytest
- psutil

## Project Overview

This project exposes system health data through REST API endpoints. The application is containerized using Docker and deployed on Kubernetes using a Deployment, Service, and ConfigMap.

The project demonstrates core DevOps concepts such as:

- Docker image creation
- Kubernetes application deployment
- Liveness and readiness probes
- ConfigMap-based configuration
- Resource requests and limits
- Shell scripting for automation
- GitHub Actions CI/CD pipeline
- Automated testing with pytest

## Architecture

```text
User / Browser / curl
        |
        v
NodePort Service
        |
        v
Kubernetes Deployment
        |
        v
Pod: Gunicorn + Flask API
        |
        v
System Metrics using psutil
API Endpoints
Endpoint	Purpose
/health	Returns CPU, memory, disk usage, and health status
/metrics	Returns system metrics with configured threshold values
/ready	Readiness endpoint used by Kubernetes
/live	Liveness endpoint used by Kubernetes
Example /health response:

{
  "cpu": 12.5,
  "memory": 45.2,
  "disk": 22.1,
  "status": "healthy"
}
Project Structure

kubernetes-system-health-api/
  .github/
    workflows/
      deploy.yml
  k8s/
    configmap.yaml
    deployment.yaml
    service.yaml
  scripts/
    build-image.sh
    deploy-k8s.sh
    check-health.sh
  app.py
  Dockerfile
  README.md
  requirements.txt
  requirements-dev.txt
  test_app.py
  
Local Docker Setup
Build the Docker image:

docker build -t system-health-api:latest .
Run the container:

docker run -p 5000:5000 system-health-api:latest
Test the API:

curl http://localhost:5000/health
curl http://localhost:5000/metrics
curl http://localhost:5000/live
curl http://localhost:5000/ready
Kubernetes Deployment
Apply the Kubernetes manifests:

kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Check pod status:

kubectl get pods
Check service:

kubectl get svc
Check rollout status:

kubectl rollout status deployment/system-health-deployment
Test the API through NodePort:

curl http://localhost:30007/health
curl http://localhost:30007/metrics
Shell Scripts
The scripts/ folder contains simple Bash scripts to automate common DevOps tasks.

Build Docker image:

bash scripts/build-image.sh
Deploy Kubernetes manifests:

bash scripts/deploy-k8s.sh
Check application health:

bash scripts/check-health.sh
You can also pass a custom URL to the health check script:

bash scripts/check-health.sh http://localhost:30007/health
Updating ConfigMap Values
Threshold values are stored in k8s/configmap.yaml.

After updating ConfigMap values, apply the ConfigMap again:

kubectl apply -f k8s/configmap.yaml
Because the application reads ConfigMap values as environment variables, restart the Deployment so pods pick up the new values:

kubectl rollout restart deployment/system-health-deployment
Running Tests
Install development dependencies:

pip install -r requirements-dev.txt
Run tests:

pytest test_app.py -v
The tests validate:

API endpoint availability
JSON response structure
health status response
readiness and liveness endpoints
threshold values in metrics response
healthy and unhealthy status behavior using mocked system metrics
CI/CD Pipeline
GitHub Actions pipeline includes three stages:

Test
Runs pytest before building the image.

Build
Builds the Docker image and pushes it to Docker Hub with two tags:

latest
Git commit SHA
Deploy
Updates the Kubernetes deployment image to the Git commit SHA tag and applies Kubernetes manifests.

Using the Git commit SHA as an image tag makes deployments traceable to the exact code version.

Kubernetes Features Used
Deployment with 2 replicas
NodePort Service
ConfigMap for threshold configuration
Liveness probe using /live
Readiness probe using /ready
Resource requests and limits
Rolling deployment using Kubernetes Deployment controller
Docker Improvements
The Dockerfile uses:

python:3.10-slim base image
Gunicorn instead of Flask development server
Runtime-only dependencies from requirements.txt
Non-root user for safer container execution
Unbuffered Python logs for better container logging
Lessons Learned
Kubernetes probes should use dedicated endpoints for liveness and readiness.
ConfigMaps help externalize configuration without changing code or rebuilding the Docker image.
ConfigMap values used as environment variables require pod restart to reflect updates.
Git commit SHA image tags make deployments easier to trace and debug.
CI/CD pipelines should fail clearly when tests, builds, or deployments fail.
Runtime and development dependencies should be separated to keep Docker images cleaner.
Shell scripts help automate repeated DevOps tasks like image builds, Kubernetes deployment, and health checks.
Future Improvements
Add Ingress support
Add Helm chart
Add Prometheus metrics endpoint
Add Grafana dashboard
Add Terraform-based infrastructure provisioning
Add security scanning in CI/CD
