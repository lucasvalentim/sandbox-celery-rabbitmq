# Makefile sandbox-celery-rabbitmq

# These targets are not files

.PHONY: all help

all: help requirements check_rabbitmq clean celery celery.beat celery.purge celery.kill celery.two celery.ten pep8 rabbitmq.config

help:
	@echo 'Makefile *** alpha *** Makefile'

requirements:
	@pip install -r requirements.txt

check_rabbitmq:
	@python check_rabbitmq_connection_2.py

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

pep8:
	@pycodestyle --filename="*.py" --ignore=W --exclude="manage.py,settings.py,migrations" --show-source --show-pep8 --statistics --count --format='%(path)s|%(row)d|%(col)d| [%(code)s] %(text)s' .

celery:
	@celery -A tasks worker --loglevel=INFO -c 1 -Q default

celery.two:
	@celery -A tasks worker --loglevel=INFO -c 2 -Q default

celery.ten:
	@celery -A tasks worker --loglevel=INFO -c 10 -Q default

celery.beat:
	@celery -A tasks beat

celery.purge:
	"from celery.task.control import discard_all; discard_all()" | python

celery.kill:
	@kill `ps -ef | grep "celery" | awk '{print $$2}'`

rabbitmq.config:
	@rabbitmqctl add_user sandbox_user sandbox_password
	@rabbitmqctl add_vhost sandbox_host
	@rabbitmqctl set_permissions -p sandbox_host sandbox_user ".*" ".*" ".*"
