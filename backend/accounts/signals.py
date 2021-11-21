from django.db.models.signals import post_save, post_delete, m2m_changed
from graphene_subscriptions.signals import post_save_subscription, post_delete_subscription

from accounts.models import Chat,Message

post_save.connect(post_save_subscription, sender=Chat, dispatch_uid="chat_post_save")

post_delete.connect(post_delete_subscription, sender=Chat,
                    dispatch_uid="chat_delete")

post_save.connect(post_save_subscription, sender=Message, dispatch_uid="message_post_save")

post_delete.connect(post_delete_subscription, sender=Message,
                    dispatch_uid="message_delete")