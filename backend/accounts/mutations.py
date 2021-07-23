import graphene
from .models import AnswersCounting, Datings, UserScaleAnswer, UserOptionAnswer
from questions.models import QuestionWithScale, QuestionWithOption, AnswerScale, AnswerOption
from users.models import CustomUser
from .types import AnswersCountingType, MatchType, UserScaleAnswerType, UserOptionAnswerType
from django.db.models import Q

class CreateUserOptionAnswerMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        question_id = graphene.ID(required=True)
        answer_id = graphene.ID(required=True)

    user_option_answer = graphene.Field(UserOptionAnswerType)

    @classmethod
    def mutate(cls, root, info, user_id, question_id, answer_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            try:
                question_with_option = QuestionWithOption.objects.get(
                    pk=question_id)
                exist_answers_count = UserOptionAnswer.objects.filter(
                    question_with_option=question_with_option, user=user).count()
                if (exist_answers_count == 0):
                    print("*****")
                    try:
                        answer_option = AnswerOption.objects.get(
                            pk=answer_id)
                        user_option_answer = UserOptionAnswer.objects.create(
                            question_with_option=question_with_option, user=user, answer=answer_option)
                        return CreateUserOptionAnswerMutation(user_option_answer=user_option_answer)
                    except AnswerOption.DoesNotExist:
                        print("****")
                        return None
                else:
                    try:
                        answer_option = AnswerOption.objects.get(
                            pk=answer_id)
                        try:
                            user_option_answer = UserOptionAnswer.objects.get(
                                question_with_option=question_with_option, user=user)
                            # print(user_option_answer)
                            user_option_answer.answer = answer_option
                            user_option_answer.save()
                            print(user_option_answer)
                            return CreateUserOptionAnswerMutation(user_option_answer=user_option_answer)
                        except UserOptionAnswer.DoesNotExist:
                            print("**-**")
                            return None
                    except AnswerOption.DoesNotExist:
                        print("***")
                        return None
            except QuestionWithOption.DoesNotExist:
                print("**")
                return None
        except CustomUser.DoesNotExist:
            print("*")
            return None


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

# Заблокировать метч
class BlockUserMatchMutation(graphene.Mutation):
    class Arguments:
        user_1 = graphene.ID(required=True)
        user_2 = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_1, user_2):
        match = Datings.objects.all().filter((Q(user_1=user_1) & Q(user_2=user_2)) | (Q(user_1=user_2) & Q(user_2=user_1)))
        print(match)
        for element in match:
            element.blocked = True
            element.save()

        return cls(ok=True)

