from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

def get_pod_logs(namespace, pod_name):
    return v1.read_namespaced_pod_log(
        name=pod_name,
        namespace=namespace,
        tail_lines=50
    )

def get_pod_events(namespace, pod_name):
    events = v1.list_namespaced_event(namespace)

    result = []

    for event in events.items:
        if event.involved_object.name == pod_name:
            result.append(event.message)

    return result

def get_pod_status(namespace, pod_name):
    pod = v1.read_namespaced_pod(pod_name, namespace)

    return {
        "phase": pod.status.phase,
        "container_status": str(pod.status.container_statuses)
    }
