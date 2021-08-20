import graphene
from graphene_django.types import DjangoObjectType
from graphene_subscriptions.events import CREATED
from rx import Observable
from .models import Datings


class DatingsType(DjangoObjectType):
    class Meta:
        model = Datings


class YourSubscription(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return Observable.interval(3000) \
                         .map(lambda i: "hello world!")