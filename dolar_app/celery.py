from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dolar_app.settings')

app = Celery('dolar_app')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'update_dolar_values': {
        'task': 'dolar.tasks.update_dolar_vals',
        'schedule': 60,
    },
}

app.autodiscover_tasks()
