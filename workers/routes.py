from loafer.ext.aws.routes import SQSRoute
from .handlers import handler_add, error_handler

routes = (
    SQSRoute('loafer-test', {'options': {'WaitTimeSeconds': 3}},
             handler=handler_add,
             error_handler=error_handler),
)
