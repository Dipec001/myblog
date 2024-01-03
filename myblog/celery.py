# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')  # Adjust 'myblog.settings' to your project's settings

# app = Celery('myblog')  # Adjust 'myblog' to your project's name

# # Load task modules from all registered Django app configs.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Autodiscover tasks from all registered apps
# app.autodiscover_tasks()





# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

app = Celery('myblog')

app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Lagos')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Discover and auto-register tasks in all installed apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
