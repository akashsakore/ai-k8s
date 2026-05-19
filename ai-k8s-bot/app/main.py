from fastapi import FastAPI
from k8s_client import *
from llm_engine import analyze_issue

app = FastAPI()

@app.get("/analyze")
def analyze(namespace: str, pod: str):

    logs = get_pod_logs(namespace, pod)
    events = get_pod_events(namespace, pod)
    status = get_pod_status(namespace, pod)

    result = analyze_issue(logs, events, status)

    return {
        "analysis": result
    }
