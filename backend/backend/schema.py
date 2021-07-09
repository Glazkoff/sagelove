import graphene
import questions.schema
import users.schema
import accounts.schema


class Query(questions.schema.Query, users.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(users.schema.Mutation, accounts.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
