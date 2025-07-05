from kubernetes import client, config
from datetime import datetime, timezone

def get_pod_status(namespace: str = "default"):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)
    pod_info = []

    for pod in pods.items:
        start_time = pod.status.start_time
        age = "-"
        if start_time:
            age_seconds = (datetime.now(timezone.utc) - start_time).total_seconds()
            age = f"{int(age_seconds // 60)} mins"

        pod_info.append({
            "name": pod.metadata.name,
            "status": pod.status.phase,
            "age": age
        })

    return pod_info