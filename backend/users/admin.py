from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(CustomUser)

admin.site.site_header = "Админпанель сайта"
admin.site.site_title = "Админпанель"
admin.site.index_title = "Административная часть сайта"
