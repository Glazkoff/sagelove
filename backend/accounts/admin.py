from .models import AnswersCounting, Datings, UserScaleAnswer, UserOptionAnswer
from django.contrib import admin
# Register your models here.


class AnswersCountingAdmin(admin.ModelAdmin):
    """Подсчет ответов"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('user', 'answers_count1', 'answers_count2',
                    'answers_count3', 'answers_count4', 'answers_count5')
    # list_filter = ('',)
    search_fields = ('user__first_name', 'user__email',)
    readonly_fields = ('user', 'answers_count1', 'answers_count2',
                       'answers_count3', 'answers_count4', 'answers_count5',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Количество ответов', {
            'fields': ('answers_count1', 'answers_count2', 'answers_count3', 'answers_count4', 'answers_count5',)
        }),
    )


class UserScaleAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('user', 'answer_scale_line', 'answer',)
    list_filter = ('user',)
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
    list_display = ('id', 'user_1', 'user_2', 'algorithm',)
    # list_filter = ('')
    search_fields = ('user_1', 'user_2',)
    fieldsets = (
        (None, {
            'fields': ('user_1', 'user_2', 'algorithm',)
        }),
    )


class UserOptionAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('user', 'question_with_option', 'answer',)
    list_filter = ('user',)
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
