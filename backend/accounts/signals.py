from django.db.models.signals import post_save, post_delete
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from accounts.models import Chat

# TODO: delete it


def test(sender, instance, **kwargs):
    print("TEST")
    print(instance)


post_save.connect(test, sender=Chat,
                  dispatch_uid="chat_save_1")

post_save.connect(post_save_subscription, sender=Chat,
                  dispatch_uid="chat_save_")

post_delete.connect(post_delete_subscription, sender=Chat,
                    dispatch_uid="chat_delete")
