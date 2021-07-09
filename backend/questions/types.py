import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption


class GroupQuestionType(DjangoObjectType):
    order_number = graphene.Int()
    next_group_id = graphene.ID()
    prev_group_id = graphene.ID()

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

    def resolve_next_group_id(self, info):
        groups = GroupQuestion.objects.all().order_by('pk')
        next_group_id = None
        is_found = False
        for group in groups:
            if group.id == self.id:
                is_found = True
                continue
            if is_found:
                next_group_id = group.id
        return next_group_id

    def resolve_prev_group_id(self, info):
        groups = GroupQuestion.objects.all().order_by('pk')
        is_first = True
        prev_group_id = None
        prev_buffer = 0
        for group in groups:
            if not is_first and self.id == group.id:
                prev_group_id = prev_buffer
                break
            if prev_buffer == 0:
                is_first = False
            prev_buffer = group.id
        return prev_group_id


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
