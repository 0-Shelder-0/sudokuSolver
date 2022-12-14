import json
import sys
from os import environ

import pika

from request_sender import send_request_to_create_status, send_request_to_update_solution
from sudoku_solver import get_solution

QUEUE_NAME = 'solutions'


def handle_message(ch, method, properties, body):
    request_json = json.loads(body.decode('utf-8'))
    solution_id = int(request_json['id'])

    try:
        send_request_to_create_status(solution_id)
        solution = get_solution(request_json['solution'])
        send_request_to_update_solution(solution, solution_id)
    except:
        print(f'Error with solution: {solution_id}')
        # response = send_request_to_create_error_status(solution_id)
        # if not response.ok:
        #     print(response)


def main():
    connection = pika.BlockingConnection(pika.URLParameters(environ.get('RABBITMQ_URL')))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=handle_message)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
