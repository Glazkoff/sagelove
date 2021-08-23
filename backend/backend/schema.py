from rx import Observable
import graphene
import questions.schema
import users.schema
import accounts.schema


class Query(accounts.schema.Query, questions.schema.Query, users.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(users.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


class Subscription(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return Observable.interval(3000) \
                         .map(lambda i: f"hello world! {i}")


schema = graphene.Schema(query=Query,
                         mutation=Mutation,
                         subscription=Subscription)
