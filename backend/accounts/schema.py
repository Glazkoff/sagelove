import graphene
from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer
from questions.models import GroupQuestion
from users.models import CustomUser
from .types import AnswersCountingType, UserScaleAnswerType, UserOptionAnswerType
from .mutations import CreateUserScaleAnswerMutation, CreateUserOptionAnswerMutation, FinishUserTesting


class Query(graphene.ObjectType):
    user_group_scale_answers = graphene.List(
        UserScaleAnswerType, user_id=graphene.ID(), group_id=graphene.ID())
    user_group_option_answers = graphene.List(
        UserOptionAnswerType, user_id=graphene.ID(), group_id=graphene.ID())

    def resolve_user_group_scale_answers(self, info, user_id, group_id):
        try:
            group = GroupQuestion.objects.get(pk=group_id)
            user = CustomUser.objects.get(pk=user_id)
            return UserScaleAnswer.objects.filter(user=user, answer_scale_line__question__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None

    def resolve_user_group_option_answers(self, info, user_id, group_id):
        try:
            group = GroupQuestion.objects.get(pk=group_id)
            user = CustomUser.objects.get(pk=user_id)
            return UserOptionAnswer.objects.filter(user=user, question_with_option__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()
    create_user_option_answer = CreateUserOptionAnswerMutation.Field()
    finish_user_testing = FinishUserTesting.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
