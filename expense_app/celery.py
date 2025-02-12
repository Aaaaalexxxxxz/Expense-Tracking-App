# project/celery.py

import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_app.settings')

# Create Celery instance
celery_app = Celery('expense_app')

# Load task modules from all Django apps
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks
celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
