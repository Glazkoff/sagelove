from transliterate import translit
from django.core.files.base import ContentFile, File
import os
import datetime
import graphene
from .models import CustomUser
from .types import CustomUserType
from accounts.models import UserScaleAnswer, UserOptionAnswer
from graphene_file_upload.scalars import Upload


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

# Обновление результатов по тесту и сведений об оплате


class UpdateUserTestResultDemoMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        test_result_demo = graphene.String(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, test_result_demo):
        user = CustomUser.objects.get(pk=user_id)
        user.test_result_demo = test_result_demo
        user.save()

        return UpdateUserTestResultDemoMutation(user=user)

#  Обновление статуса просмотра поздравления о прохождении тестировании пользователем


class UpdateUserCongratulationStatusMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        congratulations_after_test = graphene.Boolean(required=True)

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, congratulations_after_test):
        user = CustomUser.objects.get(pk=user_id)
        user.congratulations_after_test = congratulations_after_test
        user.save()

        return UpdateUserCongratulationStatusMutation(user=user)


# Мутация изменения поля "О себе" пользователя
class UpdateUserInformation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        about_me = graphene.String(required=True)
        photo = Upload()

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, about_me, photo=None):
        try:
            now = datetime.datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
            user = CustomUser.objects.get(pk=user_id)
            if photo is not None:
                filename, extension = os.path.splitext(
                    photo.name)
                first_name = translit(
                    user.first_name, language_code='ru', reversed=True)
                new_filename = f"{first_name}_photo_{now}{extension}"
                user.photo.save(
                    new_filename, File(photo))
            user.about_me = about_me
            user.save()

            return UpdateUserInformation(user=user)
        except:
            return UpdateUserInformation(user=None)


class UploadUserPhoto(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        photo = Upload()

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, photo=None):
        try:
            now = datetime.datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
            user = CustomUser.objects.get(pk=user_id)
            if photo is not None:
                filename, extension = os.path.splitext(
                    photo.name)
                first_name = translit(
                    user.first_name, language_code='ru', reversed=True)
                new_filename = f"{first_name}_photo_{now}{extension}"
                user.photo.save(
                    new_filename, File(photo))
            user.save()
            return UploadUserPhoto(user=user)
        except:
            return UploadUserPhoto(user=None)


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
