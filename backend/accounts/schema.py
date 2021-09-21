from .types import UserScaleAnswerType, UserOptionAnswerType, AnswersCountingType, MatchType, ChatType, MessageType
from .mutations import CreateMessage, CreateUserScaleAnswerMutation, CreateUserOptionAnswerMutation, DeleteChat, FinishUserTesting, BlockUserMatchMutation, CreateChat

from django.db.models import Q
import graphene

from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer, Datings, Chat, Message
from questions.models import GroupQuestion, QuestionWithScale, QuestionWithOption
from questions.types import GroupQuestionType
from users.models import CustomUser
from django.db.models import Max
from graphene_subscriptions.events import CREATED


class Query(graphene.ObjectType):
    user_group_scale_answers = graphene.List(
        UserScaleAnswerType, user_id=graphene.ID(), question_group_order=graphene.ID())
    user_group_option_answers = graphene.List(
        UserOptionAnswerType, user_id=graphene.ID(), question_group_order=graphene.ID())
    user_last_group = graphene.Field(GroupQuestionType, user_id=graphene.ID())
    matches = graphene.List(MatchType)
    match = graphene.Field(MatchType, match_id=graphene.ID())
    match_for_user = graphene.List(MatchType, user_id=graphene.ID())
    chats_for_user = graphene.List(ChatType, user_id=graphene.ID())
    messages_for_chat = graphene.List(
        MessageType, chat_id=graphene.ID(), first=graphene.Int(), skip=graphene.Int())
    chat = graphene.Field(ChatType, chat_id=graphene.ID())

    def resolve_user_group_scale_answers(self, info, user_id, question_group_order):
        try:
            group = GroupQuestion.objects.get(order=question_group_order)
            user = CustomUser.objects.get(pk=user_id)
            return UserScaleAnswer.objects.filter(user=user, answer_scale_line__question__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None

    def resolve_user_group_option_answers(self, info, user_id, question_group_order):
        try:
            group = GroupQuestion.objects.get(order=question_group_order)
            user = CustomUser.objects.get(pk=user_id)
            return UserOptionAnswer.objects.filter(user=user, question_with_option__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None

    def resolve_user_last_group(self, info, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            option_answers_max_pk = UserOptionAnswer.objects.filter(
                user=user).aggregate(
                Max("question_with_option__question_group__order"))['question_with_option__question_group__order__max']
            scale_answers_max_pk = UserScaleAnswer.objects.filter(
                user=user).aggregate(
                Max("answer_scale_line__question__question_group__order"))['answer_scale_line__question__question_group__order__max']
            pk = GroupQuestion.objects.first().order
            if option_answers_max_pk and scale_answers_max_pk:
                if option_answers_max_pk > scale_answers_max_pk:
                    pk = option_answers_max_pk
                else:
                    pk = scale_answers_max_pk
            elif option_answers_max_pk:
                pk = option_answers_max_pk
            elif scale_answers_max_pk:
                pk = scale_answers_max_pk
            return GroupQuestion.objects.get(order=pk)
        except (CustomUser.DoesNotExist):
            return None
        except:
            return None

    def resolve_matches(self, info, **kwargs):
        return Datings.objects.all()

    def resolve_match(self, info, match_id):
        return Datings.objects.get(pk=match_id)

    def resolve_match_for_user(self, info, user_id):
        return Datings.objects.all().filter((Q(user_1=user_id) | Q(user_2=user_id)) & Q(blocked=False))

    def resolve_chats_for_user(self, info, user_id):
        try:
            return Chat.objects.all().filter((Q(user_1=user_id) | Q(user_2=user_id)))
        except (Chat.DoesNotExist, CustomUser.DoesNotExist):
            return None

    def resolve_messages_for_chat(self, info, chat_id, skip, first):
        try:
            qs = Message.objects.all().filter(Q(chat=chat_id))
            if skip:
                qs = qs[skip:]
            if first:
                qs = qs[:first]
            return qs
        except (Chat.DoesNotExist, Message.DoesNotExist):
            return None

    def resolve_chat(self, info, chat_id):
        try:
            chat = Chat.objects.get(pk=chat_id)
            return chat
        except:
            return None


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()
    create_user_option_answer = CreateUserOptionAnswerMutation.Field()
    finish_user_testing = FinishUserTesting.Field()
    block_user_match = BlockUserMatchMutation.Field()
    create_chat = CreateChat.Field()
    delete_chat = DeleteChat.Field()
    create_message = CreateMessage.Field()


# class Subscription(graphene.ObjectType):
#     message_created = graphene.Field(MessageType)

#     def resolve_message_created(root, info):
#         return root.filter(
#             lambda event:
#                 event.operation == CREATED and
#                 isinstance(event.instance, Message)
#         ).map(lambda event: event.instance)


schema = graphene.Schema(query=Query,
                         mutation=Mutation)
