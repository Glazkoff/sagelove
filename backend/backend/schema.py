
from users.models import CustomUser
from accounts.models import Message, Chat
from accounts.types import MessageType, ChatType
from rx import Observable
import graphene
import questions.schema
import users.schema
import accounts.schema
from graphene_subscriptions.events import CREATED, UPDATED, DELETED


class Query(accounts.schema.Query, questions.schema.Query, users.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(users.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


class Subscription(graphene.ObjectType):
    # hello = graphene.String()
    chat_created = graphene.Field(ChatType, user_id=graphene.ID())
    message_created = graphene.Field(MessageType, chat_id=graphene.ID())
    chat_deleted = graphene.Field(ChatType, id=graphene.ID())
    chat_updated = graphene.Field(ChatType, id=graphene.ID())

    def resolve_chat_updated(root, info, id):
        return root.filter(
            lambda event:
                event.operation == UPDATED and
                isinstance(event.instance, ChatType) and
                event.instance.pk == int(id)
        ).map(lambda event: event.instance)

    def resolve_chat_created(root, info, user_id):
        user = CustomUser.objects.get(pk=user_id)
        return root.filter(
            lambda event:
                event.operation == CREATED and
                isinstance(event.instance, Chat) and
                ((event.instance.user_1 == user) or (
                    event.instance.user_2 == user))
        ).map(lambda event: event.instance)

    def resolve_message_created(root, info, chat_id):
        chat = Chat.objects.get(pk=chat_id)
        return root.filter(
            lambda event:
            event.operation == CREATED and
            isinstance(event.instance, Message) and
            (event.instance.chat == chat)
        ).map(lambda event: event.instance)

    def resolve_chat_deleted(root, info, id):
        return root.filter(
            lambda event:
                event.operation == DELETED and
                isinstance(event.instance, Chat) and
                event.instance.pk == int(id)
        ).map(lambda event: event.instance)

    # def resolve_hello(root, info):
    #     print("********************************")
    #     return Observable.interval(3000) \
    #                      .map(lambda i: f"hello world! {i}")


schema = graphene.Schema(query=Query,
                         mutation=Mutation,
                         subscription=Subscription)
