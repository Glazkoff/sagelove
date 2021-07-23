import graphene
from .models import AnswersCounting, Datings, UserScaleAnswer, UserOptionAnswer
from .types import AnswersCountingType, MatchType, UserScaleAnswerType, UserOptionAnswerType
from .mutations import BlockUserMatchMutation, CreateUserScaleAnswerMutation, CreateUserOptionAnswerMutation
from django.db.models import Q


class Query(graphene.ObjectType):
    matches = graphene.List(MatchType)
    match = graphene.Field(MatchType, match_id=graphene.ID())
    match_for_user = graphene.List(MatchType, user_id=graphene.ID())


    def resolve_matches(self, info, **kwargs):
        return Datings.objects.all()

    def resolve_match(self, info, match_id):
        return Datings.objects.get(pk=match_id)

    def resolve_match_for_user(self, info, user_id):
        return Datings.objects.all().filter((Q(user_1=user_id) | Q(user_2=user_id)) & Q(blocked=False))


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()
    create_user_option_answer = CreateUserOptionAnswerMutation.Field()
    block_user_match = BlockUserMatchMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
