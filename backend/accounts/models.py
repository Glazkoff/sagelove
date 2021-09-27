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
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Подсчёт ответов пользователя {self.user.first_name} ({self.user.email})"

    def answers_count1(self):
        return UserScaleAnswer.objects.filter(
            user=self.user, answer=1).count()

    def answers_count2(self):
        return UserScaleAnswer.objects.filter(
            user=self.user, answer=2).count()

    def answers_count3(self):
        return UserScaleAnswer.objects.filter(
            user=self.user, answer=3).count()

    def answers_count4(self):
        return UserScaleAnswer.objects.filter(
            user=self.user, answer=4).count()

    def answers_count5(self):
        return UserScaleAnswer.objects.filter(
            user=self.user, answer=5).count()

    answers_count1.short_description = "Количество ответов '1'"
    answers_count2.short_description = "Количество ответов '2'"
    answers_count3.short_description = "Количество ответов '3'"
    answers_count4.short_description = "Количество ответов '4'"
    answers_count5.short_description = "Количество ответов '5'"

    class Meta:
        verbose_name = "Подсчет ответов"
        verbose_name_plural = "Подсчеты ответов пользователей"


class UserScaleAnswer(models.Model):
    """Ответ пользователя на вопрос со шкалой"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    answer_scale_line = models.ForeignKey(
        AnswerScale, on_delete=models.CASCADE, verbose_name="Строка вопроса со шкалой")
    answer = models.PositiveIntegerField("Значение ответа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ №{self.id} пользователя {self.user.first_name}"

    class Meta:
        verbose_name = "Ответ пользователя на вопрос со шкалой"
        verbose_name_plural = "Ответы пользователей на вопрос со шкалой"


class UserOptionAnswer(models.Model):
    """Ответ пользователя на вопрос с вариантами"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    question_with_option = models.ForeignKey(
        QuestionWithOption, on_delete=models.CASCADE, verbose_name="Вопросы с вариантами ответов")
    answer = models.ForeignKey(
        AnswerOption, on_delete=models.CASCADE, verbose_name="Значение ответа")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ответ №{self.id} пользователя {self.user.first_name}"

    class Meta:
        verbose_name = "Ответ пользователя на вопрос с вариантами"
        verbose_name_plural = "Ответы пользователей на вопрос с вариантами"


ALGORITHM_SELECTION = [
    ('A1', 'Алгоритм 1'),
    ('A2', 'Алгоритм 2'),
    ('A3', 'Алгоритм 3'),
    ('HBF', 'История по ощущениям'),
]


class Datings(models.Model):
    """Совпадения пользователей"""
    user_1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='datingsfirstuser', verbose_name="Пользователь 1")
    user_2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='datingsseconduser', verbose_name="Пользователь 2")
    algorithm = models.CharField(
        verbose_name="Алгоритм", max_length=120, choices=ALGORITHM_SELECTION, null=True, blank=True)
    blocked = models.BooleanField(
        "Совпадение было заблокировано пользователем", default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Совпадения пользователя {self.user_1.first_name}(#{self.user_1.id}) и пользователя {self.user_2.first_name}(#{self.user_2.id}) по алгоритму {self.algorithm}"

    class Meta:
        verbose_name = "Совпадения пользователя"
        verbose_name_plural = "Совпадения пользователей"


class Chat(models.Model):
    """Чаты пользователей"""
    user_1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='firstuser', verbose_name="Пользователь 1")
    user_2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='seconduser', verbose_name="Пользователь 2")

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Создание чата")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Чат пользователя {self.user_1.first_name}(#{self.user_1.id}) и пользователя {self.user_2.first_name}(#{self.user_2.id})"

    class Meta:
        verbose_name = "Чат пользователей"
        verbose_name_plural = "Чаты пользователей"


class Message(models.Model):
    """Сообщения пользователей"""
    message_author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Автор сообщения")
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, verbose_name="Чат пользователей")
    message_text = models.TextField("Текст сообщения")
    message_check = models.BooleanField(
        "Сообщение было прочитано", default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message_text

    class Meta:
        verbose_name = "Сообщение пользователей"
        verbose_name_plural = "Сообщения пользователей"
