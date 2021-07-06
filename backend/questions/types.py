import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption


class GroupQuestionType(DjangoObjectType):
    class Meta:
        model = GroupQuestion
        fields = "__all__"


class QuestionWithScaleType(DjangoObjectType):
    class Meta:
        model = QuestionWithScale
        fields = "__all__"


class QuestionWithOptionType(DjangoObjectType):
    class Meta:
        model = QuestionWithOption
        fields = "__all__"


class AnswerScaleType(DjangoObjectType):
    class Meta:
        model = AnswerScale
        fields = "__all__"


class AnswerOptionType(DjangoObjectType):
    class Meta:
        model = AnswerOption
        fields = "__all__"
