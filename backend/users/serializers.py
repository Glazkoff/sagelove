from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import GENDER_SELECTION
from .models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=200)
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    phone_number = serializers.CharField(max_length=30)
    date_of_birth = serializers.DateField(
        format=None, input_formats=None,)
    about_me = serializers.CharField(max_length=200)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.gender = self.data.get('gender')
        user.date_of_birth = self.data.get('date_of_birth')
        user.phone_number = self.data.get('phone_number')
        user.about_me = self.data.get('about_me')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'pk',
            'email',
            'phone_number',
            'gender',
            'about_me',
            'date_of_birth'
        )
        read_only_fields = ('pk', 'email', 'phone_number', )
