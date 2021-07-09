from questions.models import QuestionWithOption, QuestionWithScale, AnswerOption, AnswerScale
from users.models import CustomUser
from django.db import models

# Create your models here.


class AnswersCounting(models.Model):
    """Подсчет ответов"""
    answers_count1 = models.PositiveIntegerField("Количество ответов '1'")
    answers_count2 = models.PositiveIntegerField("Количество ответов '2'")
    answers_count3 = models.PositiveIntegerField("Количество ответов '3'")
    answers_count4 = models.PositiveIntegerField("Количество ответов '4'")
    answers_count5 = models.PositiveIntegerField("Количество ответов '5'")
    # TODO: Зафиксировать в ERD
    # date_time_counting = models.DateTimeField(
    #     verbose_name="Дата и время подсчёта")
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответы пользователя №{self.user.id} от {self.date_time_counting}"

    class Meta:
        verbose_name = "Подсчет ответов"
        verbose_name_plural = "Подсчеты ответов"


class UserScaleAnswer(models.Model):
    """Ответ пользователя на вопрос со шкалой"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    # TODO: Зафиксировать в ERD
    answer_scale_line = models.ForeignKey(
        AnswerScale, on_delete=models.CASCADE, verbose_name="Строка вопроса со шкалой")
    answer = models.PositiveIntegerField("Значение ответа")
    # TODO: Зафиксировать в ERD
    # date_time_answer = models.DateTimeField(verbose_name="Дата и время ответа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ №{self.id} пользователя {self.user.first_name}"

    class Meta:
        verbose_name = "Ответ пользователя на вопрос со шкалой"
        verbose_name_plural = "Ответы пользователя на вопрос со шкалой"


class UserOptionAnswer(models.Model):
    """Ответ пользователя на вопрос с вариантами"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    question_with_option = models.ForeignKey(
        QuestionWithOption, on_delete=models.CASCADE, verbose_name="Вопросы с вариантами ответов")
    answer = models.ForeignKey(
        AnswerOption, on_delete=models.CASCADE, verbose_name="Значение ответа")
    # TODO: Зафиксировать в ERD
    # date_time_answer = models.DateTimeField(verbose_name="Дата и время ответа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ №{self.id} пользователя {self.user.first_name}"

    class Meta:
        verbose_name = "Ответ пользователя на вопрос с вариантами"
        verbose_name_plural = "Ответы пользователя на вопрос с вариантами"
