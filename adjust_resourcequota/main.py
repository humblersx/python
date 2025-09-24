from kubernetes import client, config, watch
import time

# Load kubeconfig (use config.load_incluster_config() if running inside cluster)
config.load_kube_config()

v1 = client.CoreV1Api()

def get_resourcequotas(namespace):
    return v1.list_namespaced_resource_quota(namespace=namespace).items

def adjust_resourcequota(namespace, rq):
    # Example: Decrease quota by 20% if usage < 80%
    for resource, used in rq.status.used.items():

        # Strip out Gi and m from resource values
        hard = rq.status.hard[resource]
        hard = hard.strip("Gim")
        used = used.strip("Gim")

        # Change str to int
        used_val = int(used)
        hard_val = int(hard)

        # if used resources is less than 80% of hard limits
        if used_val < 0.8 * hard_val:
            # Set new hard limit to be 80% of what it was
            new_hard_val = int(hard_val * 0.8)

            # if new memory limit would be below 150, then keep it at 150 as the new value
            if (resource == "limits.memory" or resource == "requests.memory") and  new_hard_val < 150:
                new_hard_val = 150
            print(f"Adjusting {resource} in {namespace} from {hard_val} to {new_hard_val}")
            # Patch the ResourceQuota
            body = {
                "spec": {
                    "hard": {
                        resource: str(new_hard_val)
                    }
                }
            }
            v1.patch_namespaced_resource_quota(name="default", namespace=namespace, body=body)

def monitor_resourcequotas():
    #
    #namespaces = [ns.metadata.name for ns in v1.list_namespace().items]
    namespaces = ["88790d110937-rq-dev"]
    for ns in namespaces:
        # Get RQ data from a namespace
        rqs = get_resourcequotas(ns)

        for rq in rqs:
            adjust_resourcequota(ns, rq)

    #time.sleep(60)  # Run every minute

if __name__ == "__main__":
    monitor_resourcequotas()
