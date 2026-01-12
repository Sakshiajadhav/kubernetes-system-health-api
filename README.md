# 🚀 Kubernetes System Health API

A production-grade Python API deployed on Kubernetes that monitors real-time system metrics.  
This project demonstrates a full DevOps lifecycle: from containerization and production-server migration to Kubernetes orchestration with self-healing capabilities.

[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/)  
[![Docker](https://img.shields.io/badge/docker-20.10-blue)](https://www.docker.com/)  
[![Kubernetes](https://img.shields.io/badge/kubernetes-1.27-blue)](https://kubernetes.io/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🌟 Key Features

- Real-time monitoring of CPU, memory, and disk usage using psutil
- Production ready with Gunicorn WSGI server handling concurrent requests
- Self-healing with Kubernetes Liveness and Readiness probes
- Dynamic configuration using ConfigMaps without rebuilding the Docker image
- Service discovery via Kubernetes NodePort for external access

---

## 🏗️ Architecture Flow

```
   User / Browser
         |
         v
 NodePort Service
         |
         v
 Pod: Gunicorn + Flask API
         |
         v
 System Metrics (psutil) ```


- Application: Flask API running on Gunicorn  
- Container: Dockerized using Python-slim image  
- Deployment: Manages 2 replicas of the pod  
- ConfigMap: Injects CPU/RAM thresholds as environment variables  
- Service: Routes traffic from port 30007 to the pods

---

## 🛠️ Tech Stack

Language: Python 3.9  
Framework: Flask  
WSGI Server: Gunicorn  
Containerization: Docker  
Orchestration: Kubernetes (kubectl)  
Library: psutil for system metrics

---

## 🚀 Getting Started

### 1. Prerequisites

- Docker installed  
- Kubernetes cluster (Docker Desktop, Minikube, or Kind)  
- kubectl CLI

### 2. Local Setup


# Clone the repo

git clone https://github.com/YOUR_USERNAME/kubernetes-system-health-api.git
cd kubernetes-system-health-api

# Build the Docker image

docker build -t system-health-api:2.0 .

3. Kubernetes Deployment

Apply manifests in order:


# 1. Create the ConfigMap

kubectl apply -f configmap.yaml

# 2. Deploy the application

kubectl apply -f deployment.yaml

# 3. Expose via Service

kubectl apply -f service.yaml

4. Verify Deployment

# Check pod status (wait for 1/1 Ready)

kubectl get pods

# Test the endpoint

curl http://localhost:30007/health

📈 Lessons Learned

Initial delay for probes is important to prevent Kubernetes from killing pods before Gunicorn starts

Moving thresholds to ConfigMap allows operational changes without touching app code

Gunicorn is required for production; Flask dev server is not reliable for probes

🛡️ API Reference

Endpoint: GET /health

Response Example:

json

{
  "status": "healthy",
  "cpu": 12.5,
  "memory": 45.2,
  "disk": 22.1
}

🔮 Future Enhancements
Implement Horizontal Pod Autoscaler (HPA) based on CPU usage

Add Prometheus exporter for advanced monitoring

Integrate Ingress-NGINX for path-based routing
