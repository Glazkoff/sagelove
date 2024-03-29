from graphene_django.types import DjangoObjectType
from .models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        exclude = ("password",)
