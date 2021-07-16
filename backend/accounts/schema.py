import graphene
from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer
from .types import AnswersCountingType, UserScaleAnswerType, UserOptionAnswerType
from .mutations import CreateUserScaleAnswerMutation, CreateUserOptionAnswerMutation


# class Query(graphene.ObjectType):
#     pass


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()
    create_user_option_answer = CreateUserOptionAnswerMutation.Field()


schema = graphene.Schema(mutation=Mutation)
