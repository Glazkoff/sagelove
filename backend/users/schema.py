import graphene
from .models import CustomUser
from .types import CustomUserType
from .mutations import UpdateUserInformation, UpdateUserTestStatusMutation, UpdateAimsForUserMutation, UpdateWatchOnBoardingMutation, UpdateUserCongratulationStatusMutation, UpdateUserTestResultDemoMutation


class Query(graphene.ObjectType):
    users = graphene.List(CustomUserType)
    user = graphene.Field(CustomUserType, user_id=graphene.ID())

    def resolve_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_user(self, info, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except (CustomUser.DoesNotExist,):
            user = None
        return user


class Mutation(graphene.ObjectType):
    updateUserTestStatus = UpdateUserTestStatusMutation.Field()
    updateUserTestResultDemo = UpdateUserTestResultDemoMutation.Field()
    updateUserCongratulationStatus = UpdateUserCongratulationStatusMutation.Field()
    updateUserInformation = UpdateUserInformation.Field()
    updateAimsForUser = UpdateAimsForUserMutation.Field()
    updateWatchOnBoarding = UpdateWatchOnBoardingMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
