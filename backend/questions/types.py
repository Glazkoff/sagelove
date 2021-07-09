import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption


class GroupQuestionType(DjangoObjectType):
    order_number = graphene.Int()

    class Meta:
        model = GroupQuestion
        fields = "__all__"

    def resolve_order_number(self, info):
        groups = GroupQuestion.objects.all().order_by('pk')
        count = 0
        for group in groups:
            count += 1
            if group.id == self.id:
                break
        return count


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
