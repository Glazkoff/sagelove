import graphene
from .models import AnswersCounting, Chat, Datings, Message, UserScaleAnswer, UserOptionAnswer
from questions.models import QuestionWithScale, QuestionWithOption, AnswerScale, AnswerOption
from users.models import CustomUser
from .types import AnswersCountingType, MatchType, MessageType, UserScaleAnswerType, UserOptionAnswerType
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


# Создание чата
class CreateChat(graphene.Mutation):
    class Arguments:
        user1_id = graphene.ID(required=True)
        user2_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user1_id, user2_id):
        try:
            user_1 = CustomUser.objects.get(pk=user1_id)
            user_2 = CustomUser.objects.get(pk=user2_id)
            if user_1 is not user_2:
                if Chat.objects.all().filter((Q(user_1=user_1) & Q(user_2=user_2)) | (Q(user_1=user_2) & Q(user_2=user_1))).count() == 0:
                    Chat.objects.create(user_1=user_1, user_2=user_2)
                    return CreateChat(ok=True)
                else:
                    return CreateChat(ok=False)
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

    message = graphene.Field(MessageType)

    @classmethod
    def mutate(cls, root, info, author_id, chat_id, message_text):
        try:
            author = CustomUser.objects.get(pk=author_id)
            chat = Chat.objects.get(pk=chat_id)
            message = Message.objects.create(
                message_author=author, chat=chat, message_text=message_text, message_check=False)
            return CreateMessage(message=message)
        except:
            return CreateMessage(message=None)


class DeleteChat(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        chat_id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, chat_id):
        try:
            chat = Chat.objects.get(pk=chat_id)
            chat.delete()
            return DeleteChat(ok=True)
        except:
            return DeleteChat(ok=False)
