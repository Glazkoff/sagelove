import graphene
from .models import AnswersCounting, Chat, Datings, Message, UserScaleAnswer, UserOptionAnswer
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
            if AnswersCounting.objects.filter(user=user).count() == 0:
                AnswersCounting.objects.create(user=user)
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
        match = Datings.objects.all().filter((Q(user_1=user_1) & Q(user_2=user_2))
                                             | (Q(user_1=user_2) & Q(user_2=user_1)))
        print(match)
        for element in match:
            element.blocked = True
            element.save()

        return cls(ok=True)

# Первый алгоритм поиска партнера

class CreateDatingsFirstMutation(graphene.Mutation):
    class Arguments:
        user_first = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    count_match = graphene.Int()

    @classmethod
    def mutate(cls, root, info, user_first):
        try:
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_answers = 0
            questions_with_option = QuestionWithOption.objects.all()
            questions_with_scale = QuestionWithScale.objects.all()
            count_match = 0
            for user_second in users:
                count_answers = 0
                count_answers_line = 0
                for question_with_scale in questions_with_scale:
                    answer_scale_line_qu = AnswerScale.objects.filter(question = question_with_scale)
                    for scale_line in answer_scale_line_qu:
                        first_user_answer_scale = UserScaleAnswer.objects.filter(user=user_first,answer_scale_line = scale_line).first()
                        second_user_answer_scale = UserScaleAnswer.objects.filter(user=user_second,answer_scale_line = scale_line).first()
                        if first_user_answer_scale is not None and second_user_answer_scale is not None and first_user_answer_scale.answer == second_user_answer_scale.answer:
                            count_answers_line+=1
                    if count_answers_line == answer_scale_line_qu.count():
                        count_answers += 1
                for question_with_option in questions_with_option:
                    first_user_answer_option = UserOptionAnswer.objects.filter(user=user_first,question_with_option = question_with_option).first()
                    second_user_answer_option = UserOptionAnswer.objects.filter(user=user_second,question_with_option = question_with_option).first()
                    if first_user_answer_option is not None and second_user_answer_option is not None and first_user_answer_option.answer == second_user_answer_option.answer:
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
                ).count() == 0 and user_second.gender != first_user_data.gender and count_answers >= (45 / 64) * len(
                    questions_with_option
                ) * len(
                    questions_with_scale
                ):
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A1')
                    count_match +=1
            return CreateDatingsFirstMutation(ok=True,count_match = count_match)
        except (CustomUser.DoesNotExist,QuestionWithOption.DoesNotExist,QuestionWithScale.DoesNotExist, ):
            return CreateDatingsFirstMutation(ok=False,count_match = -1)    

# Второй алгоритм поиска партнера

class CreateDatingsSecondMutation(graphene.Mutation):
    class Arguments:
        user_first = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    count_match = graphene.Int()

    @classmethod
    def mutate(cls, root, info, user_first):
        try:
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                first_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_first,answer=1).count()
                second_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_second,answer=1).count()
                first_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_first,answer=5).count()
                second_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_second,answer=5).count()
                first_user_answer_scale_2 = UserScaleAnswer.objects.filter(user=user_first,answer=2).count()
                second_user_answer_scale_2 = UserScaleAnswer.objects.filter(user=user_second,answer=2).count()
                first_user_answer_scale_4 = UserScaleAnswer.objects.filter(user=user_first,answer=4).count()
                second_user_answer_scale_4 = UserScaleAnswer.objects.filter(user=user_second,answer=4).count()
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A2')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A2')
                    )
                ).count() == 0 and (((first_user_answer_scale_1==second_user_answer_scale_5)or(second_user_answer_scale_1==first_user_answer_scale_5))and((first_user_answer_scale_2==second_user_answer_scale_4)or(second_user_answer_scale_2==first_user_answer_scale_4))) and user_second.gender != first_user_data.gender:
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A2')
                    count_match +=1
            return CreateDatingsSecondMutation(ok=True,count_match = count_match)
        except (CustomUser.DoesNotExist,UserScaleAnswer.DoesNotExist, ):
            return CreateDatingsSecondMutation(ok=False,count_match = -1)

# Третий алгоритм поиска партнера

class CreateDatingsThirdMutation(graphene.Mutation):
    class Arguments:
        user_first = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    count_match = graphene.Int()

    @classmethod
    def mutate(cls, root, info, user_first):
        try:
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                first_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_first,answer=1).count()
                second_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_second,answer=1).count()
                first_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_first,answer=5).count()
                second_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_second,answer=5).count()
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A3')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A3')
                    )
                ).count() == 0 and first_user_answer_scale_1>=35 and second_user_answer_scale_1>=35 and first_user_answer_scale_5>=5 and second_user_answer_scale_5>=5 and user_second.gender != first_user_data.gender:
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A3')
                    count_match +=1
            return CreateDatingsThirdMutation(ok=True,count_match = count_match)
        except (CustomUser.DoesNotExist,UserScaleAnswer.DoesNotExist, ):
            return CreateDatingsThirdMutation(ok=False,count_match = -1)

# Четвертый алгоритм поиска партнера

class CreateDatingsFourthMutation(graphene.Mutation):
    class Arguments:
        user_first = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    count_match = graphene.Int()

    @classmethod
    def mutate(cls, root, info, user_first):
        try:
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                if (
                    (
                        first_user_data.number_foto_history_by_felling is not None
                        or user_second.number_foto_history_by_felling is not None
                    )
                    and user_second.gender != first_user_data.gender
                    and Datings.objects.all()
                    .filter(
                        (
                            Q(user_1=first_user_data)
                            & Q(user_2=user_second)
                            & Q(algorithm='HBF')
                        )
                        | (
                            Q(user_1=user_second)
                            & Q(user_2=first_user_data)
                            & Q(algorithm='HBF')
                        )
                    )
                    .count()
                    == 0
                    and first_user_data.number_foto_history_by_felling
                    == user_second.number_foto_history_by_felling
                ):
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='HBF')
                    count_match +=1
            return CreateDatingsFourthMutation(ok=True,count_match = count_match)
        except (CustomUser.DoesNotExist, ):
            return CreateDatingsFourthMutation(ok=False,count_match = -1)


# Создание чата
class CreateChat(graphene.Mutation):
    class Arguments:
        user1_id = graphene.ID(required=True)
        user2_id = graphene.ID(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info,user1_id,user2_id):
        try:
            user_1 = CustomUser.objects.get(pk=user1_id)
            user_2 = CustomUser.objects.get(pk=user2_id)
            if Chat.objects.all().filter((Q(user_1=user_1)& Q(user_2=user_2))| (Q(user_1=user_2)& Q(user_2=user_1))).count()== 0:
                Chat.objects.create(user_1=user_1,user_2=user_2)
                return CreateChat(ok=True)
            else:
                return CreateChat(ok=False)
        except:
            return CreateChat(ok=False)

# Создание сообщения
class CreateMessage(graphene.Mutation):
    class Arguments:
        author_id = graphene.ID(required=True)
        chat_id = graphene.ID(required=True)
        message_text = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info,author_id,chat_id,message_text):
        try:
            author = CustomUser.objects.get(pk=author_id)
            chat = Chat.objects.get(pk=chat_id)
            Message.objects.create(message_author=author,chat=chat,message_text = message_text,message_check = False)
            return CreateMessage(ok=True)
        except:
            return CreateMessage(ok=False)

class DeleteChat(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        chat_id = graphene.ID()

    @classmethod
    def mutate(cls, root, info,chat_id):
        try:
            chat = Chat.objects.get(pk=chat_id)
            chat.delete()
            return DeleteChat(ok=True)
        except:
            return DeleteChat(ok=False)