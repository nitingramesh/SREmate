# SREMate 🛠️

**SREMate** is a lightweight, containerized API toolkit built with FastAPI to help Site Reliability Engineers monitor and manage systems effectively. It provides real-time system health metrics, log access, incident simulation, and Kubernetes pod status APIs.

## 🔧 Features
- `GET /health` – Live CPU, memory, and disk usage
- `GET /logs` – Fetch service logs dynamically
- `POST /simulate-crash` – Simulate a crash for alert testing
- `GET /pods/status` – Monitor pod health in Kubernetes
- `POST /alert-test` – Trigger a test alert to webhook

## 🐳 Built With
- FastAPI
- Docker
- Python (psutil, subprocess)
- Kubernetes Python Client (for future pod status)

## 📦 How to Run
```bash
# Run locally
uvicorn app.main:app --reload

## Kubernetes Pod Status (Minikube Setup Guide)

# Install kubectl
brew install kubectl

# Install Minikube
brew install minikube

# Start local Kubernetes cluster
minikube start

# Verify cluster status
kubectl get nodes
kubectl get pods -A

# Open Swagger UI and test the endpoint
# URL: http://localhost:8000/docs
# Try /pods/status with namespace: default or kube-system

# Docker
## 🐳 Run SREMate from Docker Hub
### 🔹 Step 1: Pull the Image
docker pull nitingr05/sremate:latest
### 🔹 Step 2:
docker run -p 8000:8000 nitingr05/sremate
### 🔹 Step 3:
http://localhost:8000/docs
