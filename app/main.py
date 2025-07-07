from fastapi import FastAPI
from app.utils import system
from app.utils import logs
from fastapi import Query
from app.utils import k8s
from app.logger import logger
from app.auth import verify_api_key
from fastapi import Depends


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
    logger.info("GET /health called")
    try:
        return system.get_system_metrics()
    except Exception as e:
        logger.error(f"/health failed: {str(e)}")
        import traceback
        return {"error": str(e), "trace": traceback.format_exc()}

@app.get("/logs")
def get_logs(
    path: str = Query(..., description="Absolute path to the log file"),
    lines: int = Query(50, description="Number of lines to read from the end"),
    _: None = Depends(verify_api_key)
):
    logger.info(f"GET /logs called with path={path}, lines={lines}")
    return logs.read_last_lines(path, lines)

@app.get("/pods/status")
def pods_status(namespace: str = Query("default", description="Kubernetes namespace to inspect"), _: None = Depends(verify_api_key)
):
 
    logger.info(f"GET /pods/status called with namespace={namespace}")  
    try:
        return k8s.get_pod_status(namespace)
    except Exception as e:
        logger.error(f"Error in /pods/status: {str(e)}")  
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }