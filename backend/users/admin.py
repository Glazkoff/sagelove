from django.forms import fields
from .models import CustomUser
from django.contrib.auth.models import User
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserCreationForm(forms.ModelForm):
    """Форма для создания нового пользователя. Включает все обязательные поля, плюс повторяющий пароль."""
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Пароль ещё раз', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password2(self):
        # Проверяет совпадение двух полей с паролем
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают!")
        return password2

    def save(self, commit=True):
        # Сохраняет пароль в хешированном формате
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Форма для обновления данных пользователей. Содержит все поля пользователя, но заменяет поле пароля на хешированное отображение только для чтения.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    # Формы для созздания и редактирования пользователей
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {
         'fields': ('first_name', 'gender', 'date_of_birth', 'phone_number', 'about_me')}),
         ('Цели пользователя', {
         'fields': ('partner_type', 'purpose_meet', 'number_foto_history_by_felling',)}),
        ('Права доступа', {'fields': ('is_admin',
         'is_active', 'groups', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(CustomUser, UserAdmin)

admin.site.site_header = "Админпанель сайта SageLove"
admin.site.site_title = "Админпанель SageLove"
admin.site.index_title = "Административная часть сайта SageLove"
