from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="Awesome Project")

# Hardcoded version in the app
APP_VERSION = "eks-v0.2.0"

@app.get("/health")
def health():
    """Basic health check endpoint"""
    return {
        "status": "ok",
        "server_time": datetime.utcnow().isoformat() + "Z"
        }

@app.get("/info")
def info():
    """Return pod/container/version/time info"""
    pod_name = os.getenv("POD_NAME", "unknown-pod")
    container_name = os.getenv("CONTAINER_NAME", "unknown-container")

    return {
        "pod_name": pod_name,
        "container_name": container_name,
        "version": APP_VERSION,
        "server_time": datetime.utcnow().isoformat() + "Z"
    }
