import asyncio
from raven import Client
from loafer.ext.sentry import sentry_handler

async def print_handler(message, *args):
    print('message is {}'.format(message))
    print('args is {}'.format(args))

    await asyncio.sleep(0.1)

    return True

client = Client('https://83593e0e1ca54697a7631c1ced7adca1:d4ed7284a9244625b85eede5a7f4053b@sentry.io/1353744')

error_handler = sentry_handler(client, delete_message=False)
