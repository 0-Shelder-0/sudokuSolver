import json
import os

import pika

QUEUE_NAME = 'solutions'


def send_message_to_queue(sudoku: str):
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    web_request_body = {
        'sudoku': sudoku,
    }
    body_str = json.dumps(web_request_body)
    body_bytes = bytes(body_str, 'utf-8')

    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=body_bytes)
    connection.close()
