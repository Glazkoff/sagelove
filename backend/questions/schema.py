import graphene
from .types import GroupQuestionType, QuestionWithScaleType, AnswerScaleType, QuestionWithOptionType, AnswerOptionType
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption


class Query(graphene.ObjectType):
    question_groups = graphene.List(GroupQuestionType)
    question_groups_count = graphene.Int()

    def resolve_question_groups(self, info, **kwargs):
        return GroupQuestion.objects.all()

    def resolve_question_groups_count(self, info, **kwargs):
        return GroupQuestion.objects.count()


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
