import graphene
from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer
from .types import AnswersCountingType, UserScaleAnswerType, UserOptionAnswerType
from .mutations import CreateUserScaleAnswerMutation


# class Query(graphene.ObjectType):
#     pass


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()


schema = graphene.Schema(mutation=Mutation)
