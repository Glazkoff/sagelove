import graphene
from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer
from questions.models import QuestionWithScale, AnswerScale
from users.models import CustomUser
from .types import AnswersCountingType, UserScaleAnswerType, UserOptionAnswerType


class CreateUserScaleAnswerMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        question_id = graphene.ID(required=True)
        answer = graphene.Int(required=True)

    user_scale_answer = graphene.Field(UserScaleAnswerType)

    @classmethod
    def mutate(cls, root, info, user_id, question_id, answer):
      # TODO: переделать на UserScale
        try:
            user = CustomUser.objects.get(pk=user_id)
            try:
                question_with_scale = QuestionWithScale.objects.get(
                    pk=question_id)
                exist_answers_count = UserScaleAnswer.objects.filter(
                    question_with_scale=question_with_scale, user=user).count()
                if (exist_answers_count == 0):
                    user_scale_answer = UserScaleAnswer.objects.create(
                        question_with_scale=question_with_scale, answer=answer, user=user)
                    user_scale_answer.save()
                    return CreateUserScaleAnswerMutation(user_scale_answer=user_scale_answer)
                else:
                    return None
            except QuestionWithScale.DoesNotExist:
                return None
        except CustomUser.DoesNotExist:
            return None
