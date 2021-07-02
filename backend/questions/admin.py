from django.contrib import admin
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption
# Register your models here.


class GroupQuestionAdmin(admin.ModelAdmin):
    """Группа вопросов"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('')
    search_fields = ('name_group_question',)
    fieldsets = (
        (None, {
            'fields': ('name_group_question',)
        }),
    )


class QuestionWithScaleAdmin(admin.ModelAdmin):
    """Вопросы со шкалой"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    list_filter = ('question_group',)
    search_fields = ('question_group', 'question_text',)
    fieldsets = (
        (None, {
            'fields': ('question_text', 'question_group', 'question_number',)
        }),
    )


class AnswerScaleAdmin(admin.ModelAdmin):
    """Ответы на вопросы со шкалой"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('',)
    search_fields = ('left_answer_text', 'right_answer_text',)
    fieldsets = (
        (None, {
            'fields': ('order_number', 'left_answer_text', 'right_answer_text', 'question',)
        }),
    )


class QuestionWithOptionAdmin(admin.ModelAdmin):
    """Вопросы с вариантами"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    list_filter = ('question_group',)
    search_fields = ('question_group', 'question_text',)
    fieldsets = (
        (None, {
            'fields': ('question_text', 'question_group', 'question_number',)
        }),
    )


class AnswerOptionAdmin(admin.ModelAdmin):
    """Ответы на вопросы с вариантами"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('',)
    search_fields = ('answer_text',
                     # 'answer_value',
                     )
    fieldsets = (
        (None, {
            'fields': ('answer_text',
                       # 'answer_value',
                       'question',)
        }),
    )


admin.site.register(GroupQuestion, GroupQuestionAdmin)
admin.site.register(QuestionWithScale, QuestionWithScaleAdmin)
admin.site.register(AnswerScale, AnswerScaleAdmin)
admin.site.register(QuestionWithOption, QuestionWithOptionAdmin)
admin.site.register(AnswerOption, AnswerOptionAdmin)
