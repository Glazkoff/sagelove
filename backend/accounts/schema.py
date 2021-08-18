from .types import UserScaleAnswerType, UserOptionAnswerType, AnswersCountingType, MatchType
from .mutations import CreateUserScaleAnswerMutation, CreateUserOptionAnswerMutation, FinishUserTesting, BlockUserMatchMutation
from django.db.models import Q
import graphene

from .models import AnswersCounting, UserScaleAnswer, UserOptionAnswer, Datings
from questions.models import GroupQuestion, QuestionWithScale, QuestionWithOption
from questions.types import GroupQuestionType
from users.models import CustomUser
from django.db.models import Max


class Query(graphene.ObjectType):
    user_group_scale_answers = graphene.List(
        UserScaleAnswerType, user_id=graphene.ID(), group_id=graphene.ID())
    user_group_option_answers = graphene.List(
        UserOptionAnswerType, user_id=graphene.ID(), group_id=graphene.ID())
    user_last_group = graphene.Field(GroupQuestionType, user_id=graphene.ID())
    matches = graphene.List(MatchType)
    match = graphene.Field(MatchType, match_id=graphene.ID())
    match_for_user = graphene.List(MatchType, user_id=graphene.ID())
    # algorithm_opposite = graphene.List(user_id=graphene.ID())

    def resolve_user_group_scale_answers(self, info, user_id, group_id):
        try:
            group = GroupQuestion.objects.get(pk=group_id)
            user = CustomUser.objects.get(pk=user_id)
            return UserScaleAnswer.objects.filter(user=user, answer_scale_line__question__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None

    # # Алгоритм для противопололжностей
    # def resolve_algorithm_opposite(self, info, user_id):
    #     try:
    #         user = CustomUser.objects.get(pk=user_id)
    #         user_answers_counting = AnswersCounting.objects.get(user=user)
    #         search_gender = "NS"
    #         if user.gender == "M":
    #             search_gender = "F"
    #         elif user.gender == "F":
    #             search_gender = "M"
    #         print(search_gender)
    #         num_1 = user_answers_counting.answers_count1
    #         num_2 = user_answers_counting.answers_count2
    #         num_4 = user_answers_counting.answers_count4
    #         num_5 = user_answers_counting.answers_count5
    #         print(num_1)
    #         print(num_2)
    #         print(num_4)
    #         print(num_5)
    #         return AnswersCounting.objects.all().filter(user.gender == search_gender)
    #     except (AnswersCounting.DoesNotExist, CustomUser.DoesNotExist):
    #         return None

    def resolve_user_group_option_answers(self, info, user_id, group_id):
        try:
            group = GroupQuestion.objects.get(pk=group_id)
            user = CustomUser.objects.get(pk=user_id)
            return UserOptionAnswer.objects.filter(user=user, question_with_option__question_group=group)
        except (GroupQuestion.DoesNotExist, CustomUser.DoesNotExist):
            return None

    def resolve_user_last_group(self, info, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            option_answers_max_pk = UserOptionAnswer.objects.filter(
                user=user).aggregate(
                Max("question_with_option__question_group__id"))['question_with_option__question_group__id__max']
            scale_answers_max_pk = UserScaleAnswer.objects.filter(
                user=user).aggregate(
                Max("answer_scale_line__question__question_group__id"))['answer_scale_line__question__question_group__id__max']
            pk = GroupQuestion.objects.first().id
            if option_answers_max_pk and scale_answers_max_pk:
                if option_answers_max_pk > scale_answers_max_pk:
                    pk = option_answers_max_pk
                else:
                    pk = scale_answers_max_pk
            elif option_answers_max_pk:
                pk = option_answers_max_pk
            elif scale_answers_max_pk:
                pk = scale_answers_max_pk
            return GroupQuestion.objects.get(pk=pk)
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


class Mutation(graphene.ObjectType):
    create_user_scale_answer = CreateUserScaleAnswerMutation.Field()
    create_user_option_answer = CreateUserOptionAnswerMutation.Field()
    finish_user_testing = FinishUserTesting.Field()
    block_user_match = BlockUserMatchMutation.Field()
    # create_datings_algorithm_first = CreateDatingsFirstMutation.Field()
    # create_datings_algorithm_second = CreateDatingsSecondMutation.Field()
    # create_datings_algorithm_third = CreateDatingsThirdMutation.Field()
    # create_datings_algorithm_fourth = CreateDatingsFourthMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
