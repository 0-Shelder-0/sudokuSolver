from datetime import datetime
from os import environ

import requests

from solver.models.status import Status

API_TOKEN = environ.get("API_TOKEN")
BASE_URL = environ.get("WEB_API_BASE_URL")


def send_request_to_create_status(solution_id: int):
    web_response = send_request_to(solution_id=solution_id, status=Status.IN_PROGRESS.value)
    web_response.raise_for_status()


def send_request_to_create_error_status(solution_id: int):
    return send_request_to(solution_id=solution_id, status=Status.ERROR.value)


def send_request_to(solution_id: int, status: int):
    request_model = {
        "solution_id": solution_id,
        "status": status,
        "created_at": datetime.now().isoformat()
    }
    return send_request('post', f'{BASE_URL}/status/', request_model)


def send_request_to_update_solution(solution, solution_id):
    request_model = {
        'solution': solution
    }
    web_response = send_request('put', f'{BASE_URL}/solutions/{solution_id}', request_model)
    web_response.raise_for_status()


def send_request(method, web_url, request_model):
    headers = {'Api-token': API_TOKEN}
    return requests.request(method=method, url=web_url, json=request_model, headers=headers, timeout=10)
