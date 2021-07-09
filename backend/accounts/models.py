from questions.models import QuestionWithOption, QuestionWithScale
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
    date_time_counting = models.DateTimeField( verbose_name="Дата и время подсчёта")
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"Ответы пользователя №{self.user.id} от {self.date_time_counting}"

    class Meta:
        verbose_name = "Подсчет ответов"
        verbose_name_plural = "Подсчеты ответов"

class UserAnswer(models.Model):
    """Ответ пользователя на вопрос"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    question_with_scale = models.ForeignKey(
        QuestionWithScale, on_delete=models.CASCADE, verbose_name="Вопросы со шкалой")
    question_with_option = models.ForeignKey(
        QuestionWithOption, on_delete=models.CASCADE, verbose_name="Вопросы с вариантами ответов")
    answer = models.PositiveIntegerField("Значение ответа")
    date_time_answer = models.DateTimeField( verbose_name="Дата и время ответа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"Ответ №{self.id} пользователя {self.user.first_name}"

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"

ALGORITHM_SELECTION = [
    ('A1', 'Алгоритм 1'),
    ('A2', 'Алгоритм 2'),
    ('A3', 'Алгоритм 3'),
    ('HBF', 'История по ощущениям'),
]
class Datings(models.Model):
    """Совпадения пользователей"""
    user_1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,related_name='datingsfirstuser', verbose_name="Пользователь 1")
    user_2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,related_name='datingsseconduser',verbose_name="Пользователь 2")
    algorithm = models.CharField(
        verbose_name="Алгоритм", max_length=120, choices=ALGORITHM_SELECTION,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"Совпадения пользователя {self.user_1.first_name}(#{self.user_1.id}) и пользователя {self.user_2.first_name}(#{self.user_2.id}) по алгоритму {self.algorithm}"

    class Meta:
        verbose_name = "Совпадения пользователя"
        verbose_name_plural = "Совпадения пользователей"