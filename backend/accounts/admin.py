from .models import AnswersCounting, Datings, UserScaleAnswer, UserOptionAnswer
from django.contrib import admin
# Register your models here.


class AnswersCountingAdmin(admin.ModelAdmin):
    """Подсчет ответов"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('',)
    # search_fields=('',)
    fieldsets = (
        (None, {
            'fields': ('date_time_counting', 'user',)
        }),
        ('Количество ответов', {
            'fields': ('answers_count1', 'answers_count2', 'answers_count3', 'answers_count4', 'answers_count5',)
        }),
    )


class UserScaleAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('')
    search_fields = ('answer',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Вопрос', {
            'fields': ('answer_scale_line',)
        }),
        ('Ответы', {
            'fields': ('answer',)
        }),
    )


class DatingsAdmin(admin.ModelAdmin):
    """Совпадения пользователей"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('')
    search_fields = ('user_1', 'user_2',)
    fieldsets = (
        (None, {
            'fields': ('user_1', 'user_2', 'algorithm', 'blocked')
        }),
    )


class UserOptionAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('')
    search_fields = ('answer',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Вопрос', {
            'fields': ('question_with_option',)
        }),
        ('Ответы', {
            'fields': ('answer', )
        }),
    )


admin.site.register(AnswersCounting, AnswersCountingAdmin)
admin.site.register(UserScaleAnswer, UserScaleAnswerAdmin)
admin.site.register(UserOptionAnswer, UserOptionAnswerAdmin)
admin.site.register(Datings, DatingsAdmin)
