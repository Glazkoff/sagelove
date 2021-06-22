from django.contrib import admin
from .models import GroupQuestion, QuestionWithScale
# Register your models here.
admin.site.register(GroupQuestion)
admin.site.register(QuestionWithScale)