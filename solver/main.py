import json
import os
import sys
from typing import Optional

import pika
import redis

QUEUE_NAME = 'solutions'

cache = redis.Redis(host=os.environ['CACHE_HOST'], decode_responses=True)


def get_from_cache(cache_key: str) -> Optional[int]:
    value = cache.get(cache_key)
    return value


def set_cache(cache_key: str, status_code: int) -> None:
    cache.set(cache_key, status_code, ex=100000000000)


def get_solution(request: str) -> str:
    cache_key = f"{request}"
    solution = get_from_cache(cache_key)
    if solution is None:
        solution = solve()
        set_cache(cache_key, solution)

    return solution


def solve():
    # todo реализовать механизм решения
    return None


def handle_message(ch, method, properties, body):
    request_json = json.loads(body.decode('utf-8'))
    solution = get_solution(request_json['sudoku'])
    # todo оповестить о готовности решения


def main():
    connection = pika.BlockingConnection(pika.URLParameters(os.environ['RABBITMQ_URL']))
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
