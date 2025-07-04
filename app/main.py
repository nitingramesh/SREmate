from fastapi import FastAPI
from app.utils import system
from app.utils import logs
from fastapi import Query

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