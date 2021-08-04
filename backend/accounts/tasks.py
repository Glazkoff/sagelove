from time import sleep
from backend.celery import app
from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule, created = IntervalSchedule.objects.get_or_create(
    every=5,
    period=IntervalSchedule.SECONDS)

PeriodicTask.objects.get_or_create(interval=schedule,
                                   # we created this above.
                                   # simply describes this periodic task.
                                   name='Periodic cool',
                                   # name of task.
                                   task='accounts.tasks.periodic_cool',
                                   )


@app.task
def hello_world():
    print(f"Оно живое!")
    return True


@app.task
def periodic_cool():
    print(f"Периодически, и это работает!")
    return True
