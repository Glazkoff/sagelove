import graphene
from .models import CustomUser
from .types import CustomUserType


class UpdateUserTestStatusMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        test_status = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, test_status):
        user = CustomUser.objects.get(pk=user_id)
        # TODO: проверять есть ли ответы уже и стирать их при смене на start
        user.test_status = test_status
        user.save()

        return UpdateUserTestStatusMutation(user=user)

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
