from loafer.ext.aws.routes import SQSRoute
from .handlers import print_handler, error_handler

routes = (
    SQSRoute('loafer-test', {'options': {'WaitTimeSeconds': 3}},
             handler=print_handler,
             error_handler=error_handler),
)
