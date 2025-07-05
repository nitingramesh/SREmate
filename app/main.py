from fastapi import FastAPI
from app.utils import system
from app.utils import logs
from fastapi import Query
from app.utils import k8s

app = FastAPI(
    title="SREMate",
    description="A lightweight SRE API toolkit for system health, logs, and incident simulation.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to SREMate 🎯"}

@app.get("/health")
def health_status():
    return system.get_system_metrics()

@app.get("/logs")
def get_logs(
    path: str = Query(..., description="Absolute path to the log file"),
    lines: int = Query(50, description="Number of lines to read from the end")
):
    return logs.read_last_lines(path, lines)

@app.get("/pods/status")
def pods_status(namespace: str = Query("default", description="Kubernetes namespace to inspect")):
    try:
        return k8s.get_pod_status(namespace)
    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }