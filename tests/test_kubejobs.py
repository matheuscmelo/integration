import requests
from time import sleep
from helpers import wait_for_grafana_url_generation, create_job, stop_job
from helpers.fixtures import job_payload

VISUALIZER_URL = "http://0.0.0.0:5002"
MANAGER_URL = "http://0.0.0.0:1500"

def test_create_job(job_payload):
    response = requests.post(MANAGER_URL + '/submissions', json=job_payload)
    response_payload = response.json()
    assert response.ok
    assert response_payload
    stop_job(manager_url=MANAGER_URL, job_id=response_payload.get('job_id'))


def test_visualize_grafana():
    job_id = create_job(MANAGER_URL)
    grafana_url = wait_for_grafana_url_generation(VISUALIZER_URL, job_id)
    assert requests.get(grafana_url).ok
    stop_job(manager_url=MANAGER_URL, job_id=job_id)
