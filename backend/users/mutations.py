import os
import datetime
import graphene
from .models import CustomUser
from .types import CustomUserType
from accounts.models import UserScaleAnswer, UserOptionAnswer
from django.core.files.base import File
from transliterate import translit
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

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_id, about_me, photo=None):
        print("PHOTO!!!: ")
        print(photo)
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

# Мутация загрузки фото пользователя


class SetUserPhotoMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        photo = Upload()

    user = graphene.Field(CustomUserType)

    @classmethod
    def mutate(cls, root, info, user_id, photo=None):
        # try:
        print('PHOTO!')
        print(photo)
        user = CustomUser.objects.get(pk=user_id)
        # now = datetime.datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
        # if photo is not None:
        #     print("photo")
        #     print(photo)
        #     print("photo.name")
        #     print(photo.name)
        #     filename, extension = os.path.splitext(photo.name)
        #     if user.first_name is not None:
        #         first_name = translit(
        #             user.first_name, language_code='ru', reversed=True)
        #     else:
        #         first_name = ""

        #     if user.last_name is not None:
        #         last_name = translit(
        #             user.last_name, language_code='ru', reversed=True)
        #     else:
        #         last_name = ""
        #     new_filename = f"{first_name}_{last_name}_photo_{now}{extension}"
        #     print("new_filename", new_filename)
        #     user.photo.save(
        #         new_filename, File(photo))
        # user.save()
        return SetUserPhotoMutation(user=user)
        # except:
        #     return SetUserPhotoMutation(user=None)
