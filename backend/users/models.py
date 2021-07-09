from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth, about_me, gender, phone_number):
        if not phone_number:
            raise ValueError('Пользователь должен иметь номер телефона!')
        if not email:
            raise ValueError('Пользователь должен иметь email!')
        if not date_of_birth:
            raise ValueError('Пользователь должен иметь date_of_birth!')
        if not about_me:
            raise ValueError('Пользователь должен иметь дату рождения!')
        if not gender:
            raise ValueError('Пользователь должен иметь пол!')

        user = self.model(
            phone_number=phone_number,
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            about_me=about_me,
            gender=gender
        )
        user.is_active = True
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, phone_number):
        if not email:
            raise ValueError("Пользователь должен иметь email")
        if not password:
            raise ValueError("Пользователь должен иметь пароль")
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth="2000-10-31",
            about_me="-",
            gender="NS",
            first_name="Администратор"
        )
        user.phone_number = phone_number
        user.username = username
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
PARTHNER_SELECTION = [
    ('GM', 'Для гостевого брака'),
    ('FAM', 'Для создания семьи'),
    ('JFF', 'Для просто поболтать и вместе потусить'),
]
EXPECTATION_SELECTION = [
    ('SAME', 'Такого, как я'),
    ('ANTI', 'Мою противоположность'),
    ('MATH', 'Выбор путем математического алгоритма'),
]

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Данные пользователей"""
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name="Имя", max_length=255)
    last_name = models.CharField(
        verbose_name="Фамилия", max_length=255, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    username = models.CharField(
        verbose_name="Логин", max_length=255, null=True, blank=True)
    gender = models.CharField(
        verbose_name="Пол", max_length=20, choices=GENDER_SELECTION)
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=30)
    about_me = models.TextField("О себе")
    photoURL = models.URLField("Фото", null=True, blank=True)
    is_active = models.BooleanField(
        verbose_name="Пользователь активирован",  default=True)
    is_admin = models.BooleanField(
        verbose_name="Пользователь является администратором", default=False)
    partner_type = models.CharField(
        verbose_name="Ищу партнера", max_length=120, choices=PARTHNER_SELECTION,null=True, blank=True)
    purpose_meet = models.CharField(
        verbose_name="Хочу встретить", max_length=120, choices=EXPECTATION_SELECTION, null=True, blank=True)
    number_foto_history_by_felling = models.PositiveIntegerField(verbose_name="Номер фото истории по ощущениям", null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"
