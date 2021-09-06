import graphene
from .types import GroupQuestionType, QuestionWithScaleType, AnswerScaleType, QuestionWithOptionType, AnswerOptionType
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption


class Query(graphene.ObjectType):
    question_group = graphene.Field(
        GroupQuestionType, question_group_order=graphene.ID())
    question_groups = graphene.List(GroupQuestionType)
    question_groups_count = graphene.Int()

    def resolve_question_group(self, info, question_group_order):
        try:
            return GroupQuestion.objects.get(order=question_group_order,published_or_not = True)
        except GroupQuestion.DoesNotExist:
            return None

    def resolve_question_groups(self, info, **kwargs):
        return GroupQuestion.objects.all()

    def resolve_question_groups_count(self, info, **kwargs):
        return GroupQuestion.objects.filter(published_or_not = True).count()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
