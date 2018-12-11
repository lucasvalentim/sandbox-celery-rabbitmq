import os
from urllib import request
from celery import Celery

BASEDIR = os.path.join(os.path.dirname(__file__), 'files')

app = Celery('downloaderApp', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def download(url, filename):
    response = request.urlopen(url)

    data = response.read()

    with open(os.path.join(BASEDIR, filename), 'wb') as file:
        file.write(data)

@app.task
def list():
    return os.listdir(BASEDIR)

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y
