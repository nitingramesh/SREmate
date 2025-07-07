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

<img width="1226" alt="Screenshot 2025-07-07 at 7 35 42 PM" src="https://github.com/user-attachments/assets/bf8ff90d-e4a4-4ba2-b6de-270cb1231b91" />
<img width="673" alt="Screenshot 2025-07-07 at 8 29 24 PM" src="https://github.com/user-attachments/assets/c61c181a-9745-44af-a610-e91587e04eb2" />
<img width="1226" alt="Screenshot 2025-07-07 at 7 35 50 PM" src="https://github.com/user-attachments/assets/c6063686-bfdb-46b2-9276-a499b44ea19e" />
<img width="1226" alt="Screenshot 2025-07-07 at 7 36 22 PM" src="https://github.com/user-attachments/assets/107e9747-8d65-4ab9-92e3-f9bd656c0fbd" />
<img width="1226" alt="Screenshot 2025-07-07 at 8 07 59 PM" src="https://github.com/user-attachments/assets/0ec1155f-520e-4735-abaa-c4fad3c313d5" />
<img width="1226" alt="Screenshot 2025-07-07 at 7 35 06 PM" src="https://github.com/user-attachments/assets/ad67cd3d-edd8-42ba-85d1-45ec4227695b" />

## 🌐 Live Demo

SREMate is now publicly hosted on Render:

🔗 https://sremate.onrender.com/docs  
Use this to test API routes live from any browser.
