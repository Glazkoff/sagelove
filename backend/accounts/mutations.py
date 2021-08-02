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
            question_with_option = QuestionWithOption.objects.get(
                pk=question_id)
            exist_answers_count = UserOptionAnswer.objects.filter(
                question_with_option=question_with_option, user=user).count()
            answer_option = AnswerOption.objects.get(
                pk=answer_id)
            if (exist_answers_count == 0):

                user_option_answer = UserOptionAnswer.objects.create(
                    question_with_option=question_with_option, user=user, answer=answer_option)
            else:
                user_option_answer = UserOptionAnswer.objects.get(
                    question_with_option=question_with_option, user=user)
                user_option_answer.answer = answer_option
                user_option_answer.save()
            return CreateUserOptionAnswerMutation(user_option_answer=user_option_answer)
        except (CustomUser.DoesNotExist, QuestionWithOption.DoesNotExist, AnswerOption.DoesNotExist, UserOptionAnswer.DoesNotExist):
            return None


class CreateUserScaleAnswerMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        question_row_id = graphene.ID(required=True)
        answer = graphene.Int(required=True)

    user_scale_answer = graphene.Field(UserScaleAnswerType)

    @classmethod
    def mutate(cls, root, info, user_id, question_row_id, answer):
        try:
            user = CustomUser.objects.get(pk=user_id)
            question_line = AnswerScale.objects.get(pk=question_row_id)
            exist_answers_count = UserScaleAnswer.objects.filter(
                answer_scale_line=question_line, user=user).count()
            if exist_answers_count == 0:
                user_scale_answer = UserScaleAnswer.objects.create(
                    answer_scale_line=question_line, user=user, answer=answer)
            else:
                user_scale_answer = UserScaleAnswer.objects.get(
                    answer_scale_line=question_line, user=user)
                user_scale_answer.answer = answer
                user_scale_answer.save()
            return CreateUserScaleAnswerMutation(user_scale_answer=user_scale_answer)
        except (CustomUser.DoesNotExist, AnswerScale.DoesNotExist, UserScaleAnswer.DoesNotExist):
            return None


class FinishUserTesting(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)

    status_ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            user.test_status = 'finish'
            user.save()
            return FinishUserTesting(status_ok=True)
        except (CustomUser.DoesNotExist, ):
            return FinishUserTesting(status_ok=False)
            
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

class CreateDatingsMutation(graphene.Mutation):
    class Arguments:
        user_first = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    count_match = graphene.Int()

    @classmethod
    def mutate(cls, root, info, user_first):
        try:
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            first_user_data = CustomUser.objects.get(pk=user_first)
            count_answers = 0
            questions_with_option = QuestionWithOption.objects.all()
            questions_with_scale = QuestionWithScale.objects.all()
            count_match = 0
            for user_second in users:
                count_answers = 0
                count_answers_line = 0
                for k in questions_with_scale:
                    answer_scale_line_qu = AnswerScale.objects.filter(question = k)
                    for w in answer_scale_line_qu:
                        c = UserScaleAnswer.objects.filter(user=user_first,answer_scale_line = w).first()
                        d = UserScaleAnswer.objects.filter(user=user_second,answer_scale_line = w).first()
                        if c.answer == d.answer:
                            count_answers_line+=1
                    if count_answers_line == len(answer_scale_line_qu):
                        count_answers+=1
                for n in questions_with_option:
                    a = UserOptionAnswer.objects.filter(user=user_first,question_with_option = n).first()
                    b = UserOptionAnswer.objects.filter(user=user_second,question_with_option = n).first()
                    if a.answer == b.answer:
                        count_answers+=1
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A1')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A1')
                    )
                ).count() == 0 and count_answers >= (45 / 64) * len(
                    questions_with_option
                ) * len(
                    questions_with_scale
                ):
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A1')
                    count_match +=1
            return CreateDatingsMutation(ok=True,count_match = count_match)
        except (CustomUser.DoesNotExist,QuestionWithOption.DoesNotExist,QuestionWithScale.DoesNotExist, ):
            return CreateDatingsMutation(ok=False,count_match = -1)    

