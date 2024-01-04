web gunicorn myblog.wsgi:application --log-file -
worker: celery -A myblog.celery worker --pool=solo -l info