import json
from os import environ

import pika

QUEUE_NAME = 'solutions'


def send_message_to_queue(solution_id: int, solution: [[]]):
    connection = pika.BlockingConnection(pika.URLParameters(environ.get('RABBITMQ_URL')))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    web_request_body = {
        'id': solution_id,
        'solution': solution,
    }
    body_str = json.dumps(web_request_body)
    body_bytes = bytes(body_str, 'utf-8')

    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=body_bytes)
    connection.close()
