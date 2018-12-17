import time
import random
import json
import boto3
from decouple import config

QUEUE_NAME = config('QUEUE_NAME')
QNT_TASKS = config('QNT_TASKS', default=100, cast=int)
DURATION = config('DURATION', default=60, cast=int)
INTERVAL = config('INTERVAL', default=1, cast=int)

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

for m in range(DURATION):
    for n in range(QNT_TASKS):
        print(m, n)

        message_body = json.dumps({
            'a': random.randint(1, 100),
            'b': random.randint(-100, 1)
        })
        
        response = queue.send_message(MessageBody=message_body)

    time.sleep(60 * INTERVAL)
