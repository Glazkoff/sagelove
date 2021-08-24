import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": URLRouter([
        path('ws/subscriptions/', GraphqlSubscriptionConsumer)
    ]),
})
