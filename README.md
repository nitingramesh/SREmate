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

# Docker
docker build -t sremate .
docker run -p 8000:8000 sremate
