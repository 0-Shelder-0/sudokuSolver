import json
from os import environ

import requests

from solver.models.status import Status

API_TOKEN = environ.get("API_TOKEN")
BASE_URL = environ.get("WEB_API_BASE_URL")


def send_request_to_create_status(solution_id: int):
    request_model = {
        'solution_id': solution_id,
        'status': Status.IN_PROGRESS.value
    }
    send_request('post', f'{BASE_URL}/status/', request_model)


def send_request_to_update_solution(solution, solution_id):
    request_model = {
        'solution': solution
    }
    send_request('put', f'{BASE_URL}/solution/{solution_id}', request_model)


def send_request(method, web_url, request_model):
    web_request_body = json.dumps(request_model)
    headers = {
        'api-token': API_TOKEN,
        "Content-type": "application/json"}

    web_response = requests.request(method=method, url=web_url, json=web_request_body, headers=headers, timeout=10)
    web_response.raise_for_status()
