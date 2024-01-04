gunicorn myblog.wsgi:application
worker: celery -A myblog.celery worker --pool=solo -l info