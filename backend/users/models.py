from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# TODO: null value in column "date_of_birth" violates not-null constraint


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth, about_me, gender, phone_number):
        if not phone_number:
            raise ValueError('Пользователь должен иметь номер телефона!')
        if not email:
            raise ValueError('Пользователь должен иметь email!')
        # if not date_of_birth:
        #     raise ValueError('Пользователь должен иметь date_of_birth!')
        if not about_me:
            raise ValueError('Пользователь должен иметь about_me!')
        if not gender:
            raise ValueError('Пользователь должен иметь gender!')

        user = self.model(
            phone_number=phone_number,
            username=username,
            email=email,
            # date_of_birth=date_of_birth,
            about_me=about_me,
            gender=gender
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password,):
        user = self.model(
            username=username,
            email=email,
            date_of_birth="2000-10-31",
            phone_number="+7 999 999 99 99",
            about_me="-",
            gender="NS"
        )
        user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


GENDER_SELECTION = [
    ('M', 'Мужской'),
    ('F', 'Женский'),
    ('NS', 'Не указан'),
]


class CustomUser(AbstractUser):
    gender = models.CharField(
        verbose_name="Пол", max_length=20, choices=GENDER_SELECTION)
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=30)
    about_me = models.TextField("О себе")
    photoURL = models.URLField("Фото", null=True, blank=True)
    objects = CustomUserManager()
