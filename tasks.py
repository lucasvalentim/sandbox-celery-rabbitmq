
import os
from urllib import request

from celery import Celery
from celery.utils.log import get_task_logger
from decouple import config

logger = get_task_logger(__name__)

BASEDIR = os.path.join(os.path.dirname(__file__), 'files')
RABBITMQ_URL = config('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')

app = Celery('tasks', backend='rpc://', broker=RABBITMQ_URL)


@app.task
def download(url, filename):
    response = request.urlopen(url)

    data = response.read()

    with open(os.path.join(BASEDIR, filename), 'wb') as file:
        file.write(data)


@app.task
def list():
    return os.listdir(BASEDIR)


@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y
