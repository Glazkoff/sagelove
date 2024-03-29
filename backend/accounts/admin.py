from .models import AnswersCounting, Datings, UserScaleAnswer, UserOptionAnswer,Chat,Message
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

    def has_add_permission(self, request, obj=None):
        return False


class UserScaleAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('user', 'answer_scale_line', 'answer',)
    list_filter = ('user',)
    search_fields = ('answer', 'user__first_name')
    readonly_fields = ('user', 'answer_scale_line', 'answer',)
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

    def has_add_permission(self, request, obj=None):
        return False


class DatingsAdmin(admin.ModelAdmin):
    """Совпадения пользователей"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('id', 'user_1', 'user_2', 'algorithm',)
    list_filter = ('algorithm',)
    search_fields = ('user_1__first_name', 'user_2__first_name',)
    fieldsets = (
        (None, {
            'fields': ('user_1', 'user_2', 'algorithm', 'blocked')
        }),
    )


class UserOptionAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    list_display = ('user', 'question_with_option', 'answer',)
    list_filter = ('user',)
    search_fields = ('answer__answer_text', 'user__first_name')
    readonly_fields = ('user', 'question_with_option', 'answer',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Вопрос', {
            'fields': ('question_with_option',)
        }),
        ('Ответ', {
            'fields': ('answer', )
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

class ChatAdmin(admin.ModelAdmin):
    """Чаты пользователей"""
    exclude = ('created_at', 'updated_at')
    list_display = ('id', 'user_1', 'user_2','created_at',)
    list_filter = ('user_1', 'user_2',)
    search_fields = ('user_1__first_name', 'user_2__first_name',)
    fieldsets = (
        (None, {
            'fields': ('user_1', 'user_2',)
        }),
    )

class MessageAdmin(admin.ModelAdmin):
    """Сообщения пользователей"""
    exclude = ('created_at', 'updated_at')
    list_display = ('chat', 'message_author', 'message_text', 'message_check',)
    search_fields = ('chat', 'message_author__first_name',)
    fieldsets = (
        (None, {
            'fields': ('message_author', 'chat','message_text', 'message_check',)
        }),
    )
    readonly_fields = ['message_check', ]

admin.site.register(AnswersCounting, AnswersCountingAdmin)
admin.site.register(UserScaleAnswer, UserScaleAnswerAdmin)
admin.site.register(UserOptionAnswer, UserOptionAnswerAdmin)
admin.site.register(Datings, DatingsAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)