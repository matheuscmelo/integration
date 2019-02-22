import requests
from time import sleep
import json

def wait_for_grafana_url_generation(visualizer_url, job_id, max_wait_time=120, max_tries=10):
    delta = max_wait_time / max_tries
    for _ in range(max_tries):
        sleep(delta)
        response = requests.get(visualizer_url + '/visualizing/{}'.format(job_id))
        if response.ok:
            url = response.json().get('url')
            if url != "URL not generated!":
                return url
    raise Exception("Max tries to get generated URL exceeded.")

def create_job(manager_url):
    job_payload = get_job_payload()
    response = requests.post(manager_url + '/submissions', json=job_payload)
    response_payload = response.json()
    job_id = response_payload.get('job_id')
    return job_id

def stop_job(manager_url, job_id):
    requests.put(manager_url + '/submissions/' + job_id, json={
        "enable_auth": False
    })


def get_job_payload():
    with open("assets/payload.json", 'r') as f:
        return json.loads(f.read())
