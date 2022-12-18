import json
from os import environ

import requests

from solver.models.solution import SolutionUpdate
from solver.models.solution_status import SolutionStatusCreate
from solver.models.status import Status

API_TOKEN = environ.get("API_TOKEN")
BASE_URL = environ.get("WEB_API_BASE_URL")


def send_request_to_create_status(solution_id: int):
    model = SolutionStatusCreate(solution_id, Status.IN_PROGRESS)
    send_request('post', f'{BASE_URL}/status/', model)


def send_request_to_update_solution(solution, solution_id):
    model = SolutionUpdate(solution_id, solution)
    send_request('put', f'{BASE_URL}/solution/{solution_id}', model)


def send_request(method, web_url, model):
    web_request_body = json.dumps(model)
    headers = {'api-token': API_TOKEN}

    web_response = requests.request(method=method, url=web_url, json=web_request_body, headers=headers, timeout=10)
    web_response.raise_for_status()
