import os

from celery import Celery
from datetime import timedelta
from kombu import Exchange, Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_queues = (
    Queue('high', Exchange('high'), routing_key='high'),
    Queue('normal',  Exchange('normal'),   routing_key='normal'),
    Queue('low',  Exchange('low'),   routing_key='low'),
)
app.conf.task_default_queue = 'normal'
app.conf.task_default_exchange_type = 'normal'
app.conf.task_default_routing_key = 'normal'

app.conf.beat_schedule = {
    # 'say_hello': {
    #     'task': 'accounts.tasks.hello_world',
    #     'schedule': 10.0
    # },
    'first_algorithm': {
        'task': 'accounts.tasks.first_algorithm',
        'schedule': timedelta(hours=1)
    },
    'second_algorithm': {
        'task': 'accounts.tasks.second_algorithm',
        'schedule': timedelta(hours=1)
    },
    'third_algorithm': {
        'task': 'accounts.tasks.third_algorithm',
        'schedule': timedelta(hours=1)
    },
    'fourth_algorithm': {
        'task': 'accounts.tasks.fourth_algorithm',
        'schedule': timedelta(hours=1)
    },
    'fifth_algorithm': {
        'task': 'accounts.tasks.fifth_algorithm',
        'schedule': timedelta(hours=1)
    },
    'sixth_algorithm': {
        'task': 'accounts.tasks.sixth_algorithm',
        'schedule': timedelta(hours=1)
    },
    'seventh_algorithm': {
        'task': 'accounts.tasks.seventh_algorithm',
        'schedule': timedelta(hours=1)
    }

}
app.conf.task_routes = {
    'first_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'second_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'third_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'fourth_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'fifth_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'sixth_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
    'seventh_algorithm': {
        'queue': 'normal',
        'routing_key': 'normal',
    },
}