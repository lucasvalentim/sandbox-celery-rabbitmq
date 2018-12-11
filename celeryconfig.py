from decouple import config

BROKER_URL = config('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672/')
SQS_ON = config('SQS_ON', default=False, cast=bool)

TASK_SERIALIZER = 'json'
RESULT_SERIALIZER = 'json'
ACCEPT_CONTENT = ['application/json']
CONTENT_ENCODING = 'utf-8'
TIMEZONE = 'America/Recife'
ENABLE_UTC = True
CELERY_ROUTES = {
    'tasks.add': {'queue': 'default'},
    'tasks.download': {'queue': 'download'},
}
CELERY_DEFAULT_QUEUE = 'default'
CELERY_IGNORE_RESULT = True

if SQS_ON:
    BROKER_TRANSPORT = 'sqs'
    SEND_EVENTS = False
    ENABLE_REMOTE_CONTROL = False
    SQS_QUEUE_NAME = 'celery-sandbox-sqs'

    BROKER_TRANSPORT_OPTIONS = {
        'region': 'us-east-1',
        'polling_interval': 60,
        'visibility_timeout': 3600,
        'queue_name_prefix': 'celery-sandbox'
    }

    # BROKER_USER = config('AWS_ACCESS_KEY_ID')
    # BROKER_PASSWORD = config('AWS_SECRET_ACCESS_KEY')
