from django.db import models

# Create your models here.


class GroupQuestion(models.Model):
    """Группа вопросов"""
    name_group_question = models.CharField("Название группы", max_length=200)
    order = models.IntegerField(verbose_name="Прядок",default=0,unique=True)
    published_or_not = models.BooleanField(
        default=False, verbose_name="Публикация")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_group_question}"

    # def order(self):
    #     groups = GroupQuestion.objects.all()
    #     order = 0
    #     for group in groups:
    #         order += 1
    #         if group.id == self.id:
    #             break
    #     return order
    # order.short_description = "Порядок"

    class Meta:
        verbose_name = "Группа вопросов"
        verbose_name_plural = "Группы вопросов"


class QuestionWithScale(models.Model):
    """Вопросы со шкалой"""
    question_text = models.TextField("Текст вопроса")
    question_group = models.ForeignKey(
        GroupQuestion, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Группа вопросов")
    question_number = models.PositiveIntegerField("Номер вопроса")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"'{self.question_text}' (группа '{self.question_group.name_group_question}')"

    class Meta:
        verbose_name = "Вопрос со шкалой"
        verbose_name_plural = "Вопросы со шкалой"


class AnswerScale(models.Model):
    """Ответы на вопросы со шкалой"""
    left_answer_text = models.TextField("Ответ с левой стороны шкалы")
    right_answer_text = models.TextField("Ответ с правой стороны шкалы")
    question = models.ForeignKey(
        QuestionWithScale, on_delete=models.CASCADE, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Строка №{self.id} ответов на вопрос {self.question.id} "

    class Meta:
        verbose_name = "Ответ на вопросы со шкалой"
        verbose_name_plural = "Ответы на вопросы со шкалой"


class QuestionWithOption(models.Model):
    """Вопросы с вариантами"""
    question_text = models.TextField("Текст вопроса")
    question_group = models.ForeignKey(
        GroupQuestion, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Группа вопросов")
    question_number = models.PositiveIntegerField("Номер вопроса")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Вопрос №{self.question_number} группы '{self.question_group.name_group_question}'"

    class Meta:
        verbose_name = "Вопрос с вариантами"
        verbose_name_plural = "Вопросы с вариантами"


class AnswerOption(models.Model):
    """Ответы на вопросы с вариантами"""
    answer_text = models.TextField("Текст варианта ответа")
    question = models.ForeignKey(
        QuestionWithOption, on_delete=models.CASCADE, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.answer_text} (вопрос {self.question.id}) "

    class Meta:
        verbose_name = "Ответ на вопросы с вариантами"
        verbose_name_plural = "Ответы на вопросы с вариантами"
