from django.contrib import admin
from .models import GroupQuestion, QuestionWithScale, AnswerScale, QuestionWithOption, AnswerOption
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.

class AnswerScaleInline(admin.StackedInline):
    """Ответы на вопросы со шкалой"""
    model = AnswerScale
    extra = 1

class AnswerOptionInline(admin.StackedInline):
    """Ответы на вопросы с вариантами"""
    model = AnswerOption
    extra = 1

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
    list_display=('__str__','question_text',"published_or_not",)
    list_filter = ('question_group',"published_or_not",)
    search_fields = ('question_group', 'question_text',)
    fieldsets = (
        (None, {
            'fields': ('question_text', 'question_group', 'question_number',)
        }),
    )
    inlines=[AnswerScaleInline]
    list_editable= ("published_or_not",)
    actions = ["published", "unpublished"]

    def unpublished(self, request,queryset):
        """Снять с публикации"""
        row_update = queryset.update(published_or_not=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def published(self, request,queryset):
        """Опубликовать"""
        row_update = queryset.update(published_or_not=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    published.short_description = "Опубликовать"
    published.allowed_permissions = ('change',)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ('change',)

    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }


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
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }



class QuestionWithOptionAdmin(admin.ModelAdmin):
    """Вопросы с вариантами"""
    exclude = ('createdAt', 'updatedAt')
    list_display=('__str__','question_text',"published_or_not",)
    list_filter = ('question_group',"published_or_not",)
    search_fields = ('question_group', 'question_text',)
    fieldsets = (
        (None, {
            'fields': ('question_text', 'question_group', 'question_number',)
        }),
    )
    inlines=[AnswerOptionInline]
    list_editable= ("published_or_not",)
    actions = ["published", "unpublished"]

    def unpublished(self, request,queryset):
        """Снять с публикации"""
        row_update = queryset.update(published_or_not=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def published(self, request,queryset):
        """Опубликовать"""
        row_update = queryset.update(published_or_not=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    published.short_description = "Опубликовать"
    published.allowed_permissions = ('change',)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ('change',)
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }


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
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }


admin.site.register(GroupQuestion, GroupQuestionAdmin)
admin.site.register(QuestionWithScale, QuestionWithScaleAdmin)
admin.site.register(AnswerScale, AnswerScaleAdmin)
admin.site.register(QuestionWithOption, QuestionWithOptionAdmin)
admin.site.register(AnswerOption, AnswerOptionAdmin)
