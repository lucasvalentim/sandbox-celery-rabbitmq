from raven import Client
from loafer.ext.sentry import sentry_handler
from utils import sum_
from decouple import config


async def handler_add(data, *args):
    return sum_(data['x'], data['y'])

client = Client(config('SENTRY_TOKEN_URL'))
error_handler = sentry_handler(client, delete_message=False)
