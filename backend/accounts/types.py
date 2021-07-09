from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer
from graphene_django.types import DjangoObjectType


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
