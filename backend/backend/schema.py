
from accounts.models import Message, Chat
from accounts.types import MessageType, ChatType
from rx import Observable
import graphene
import questions.schema
import users.schema
import accounts.schema
from graphene_subscriptions.events import CREATED, DELETED


class Query(accounts.schema.Query, questions.schema.Query, users.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(users.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


class Subscription(graphene.ObjectType):
    hello = graphene.String()
    chat_created = graphene.Field(ChatType)
    chat_deleted = graphene.Field(ChatType, id=graphene.ID())

    def resolve_chat_created(root, info):
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Chat)
        ).map(lambda event: event.instance)

    def resolve_chat_deleted(root, info, id):
        return root.filter(
            lambda event:
                event.operation == DELETED and
                isinstance(event.instance, Chat) and
                event.instance.pk == int(id)
        ).map(lambda event: event.instance)

    def resolve_hello(root, info):
        print("********************************")
        return Observable.interval(3000) \
                         .map(lambda i: f"hello world! {i}")


schema = graphene.Schema(query=Query,
                         mutation=Mutation,
                         subscription=Subscription)
