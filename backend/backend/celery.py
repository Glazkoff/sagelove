import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'say_hello': {
    #     'task': 'accounts.tasks.hello_world',
    #     'schedule': 10.0
    # },
    'first_algorithm': {
        'task': 'accounts.tasks.first_algorithm',
        'schedule': 3600.0
    },
    'second_algorithm': {
        'task': 'accounts.tasks.second_algorithm',
        'schedule': 3600.0
    },
    'third_algorithm': {
        'task': 'accounts.tasks.third_algorithm',
        'schedule': 3600.0
    },
    'fourth_algorithm': {
        'task': 'accounts.tasks.fourth_algorithm',
        'schedule': 3600.0
    }
}
