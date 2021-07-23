import graphene
from .models import CustomUser
from .types import CustomUserType
from accounts.models import UserScaleAnswer, UserOptionAnswer


class UpdateUserTestStatusMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        test_status = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, test_status):
        try:
            user = CustomUser.objects.get(pk=user_id)
            user.test_status = test_status
            if test_status == 'start':
                UserScaleAnswer.objects.filter(user=user).delete()
                UserOptionAnswer.objects.filter(user=user).delete()
            user.save()
            return UpdateUserTestStatusMutation(user=user)
        except (CustomUser.DoesNotExist,):
            return UpdateUserTestStatusMutation(user=None)

# Мутация изменения поля "О себе" пользователя


class UpdateUserInformation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        about_me = graphene.String(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_id, about_me):
        user = CustomUser.objects.get(pk=user_id)
        user.about_me = about_me
        user.save()

        return cls(ok=True)


class AimsInput(graphene.InputObjectType):
    partner_type = graphene.String(required=True)
    purpose_meet = graphene.String(required=True)
    number_foto_history_by_felling = graphene.Int(required=True)
    user_id = graphene.ID(required=True)

# Мутация создания или изменения целей пользователя

class UpdateAimsForUserMutation(graphene.Mutation):
    class Arguments:
        aims_data = AimsInput(required=True)

    user = graphene.Field(CustomUserType)

    def mutate(root, info, aims_data=None):
        user = CustomUser.objects.get(pk=aims_data.user_id)
        user.partner_type = aims_data.partner_type
        user.purpose_meet = aims_data.purpose_meet
        user.number_foto_history_by_felling = aims_data.number_foto_history_by_felling
        user.save()
        return UpdateAimsForUserMutation(user=user)

# Мутация изменения статуса просмотра on-boarding 
class UpdateWatchOnBoardingMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        watch_on_boarding = graphene.Boolean(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, watch_on_boarding):
        user = CustomUser.objects.get(pk=user_id)
        user.watch_on_boarding = watch_on_boarding
        user.save()

        return UpdateWatchOnBoardingMutation(user=user)

