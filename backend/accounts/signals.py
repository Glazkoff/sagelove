from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from .models import Datings

post_save.connect(post_save_subscription, sender=Datings, dispatch_uid="your_model_post_save")
post_delete.connect(post_delete_subscription, sender=Datings, dispatch_uid="your_model_post_delete")

# your_app/apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals