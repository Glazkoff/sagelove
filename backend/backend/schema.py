import graphene
import questions.schema
import users.schema
import accounts.schema
from accounts.subscriptions import YourSubscription


class Query(accounts.schema.Query, questions.schema.Query, users.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(users.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass

class Subscription(YourSubscription):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation,subscription=Subscription)
