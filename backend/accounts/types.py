from .models import AnswersCounting, Chat, Datings, Message, UserScaleAnswer, UserOptionAnswer
from graphene_django.types import DjangoObjectType
import graphene
from django.db.models import Q
from users.models import CustomUser

class AnswersCountingType(DjangoObjectType):
    class Meta:
        model = AnswersCounting
        fields = "__all__"


class UserScaleAnswerType(DjangoObjectType):
    class Meta:
        model = UserScaleAnswer
        fields = "__all__"


class UserOptionAnswerType(DjangoObjectType):
    class Meta:
        model = UserOptionAnswer
        fields = "__all__"


class MatchType(DjangoObjectType):
    class Meta:
        model = Datings
        fields = "__all__"


class ChatType(DjangoObjectType):
    number_messages_which_are_not_read = graphene.Int()
    class Meta:
        model = Chat
        fields = "__all__"
    def resolve_number_messages_which_are_not_read(self, info):
        return Message.objects.all().filter(Q(chat=self.id)&Q(message_check=False)).exclude(message_author = CustomUser.objects.get(pk=info.variable_values['userId'])).count()
class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = "__all__"