from time import sleep
from backend.celery import app
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import graphene
from .models import Datings, UserScaleAnswer, UserOptionAnswer
from questions.models import QuestionWithScale, QuestionWithOption, AnswerScale
from users.models import CustomUser
from django.db.models import Q

schedule, created = IntervalSchedule.objects.get_or_create(
    every=5,
    period=IntervalSchedule.SECONDS)

PeriodicTask.objects.get_or_create(interval=schedule,
                                   # we created this above.
                                   # simply describes this periodic task.
                                   name='Periodic cool',
                                   # name of task.
                                   task='accounts.tasks.periodic_cool',
                                   )


# @app.task
# def hello_world():
#     print(f"Оно живое!")
#     return True


@app.task
def periodic_cool():
    print(f"Периодически, и это работает!")
    return True

# Первый алгоритм поиска партнеров

@app.task
def first_algorithm():
    try:
        users_all = CustomUser.objects.all().filter(test_status = 'finish')
        for user in users_all:
            user_first = user.id
            ok = graphene.Boolean()
            count_match = graphene.Int()
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_answers = 0
            questions_with_option = QuestionWithOption.objects.all()
            questions_with_scale = QuestionWithScale.objects.all()
            count_match = 0
            for user_second in users:
                count_answers = 0
                count_answers_line = 0
                for question_with_scale in questions_with_scale:
                    answer_scale_line_qu = AnswerScale.objects.filter(question = question_with_scale)
                    for scale_line in answer_scale_line_qu:
                        first_user_answer_scale = UserScaleAnswer.objects.filter(user=user_first,answer_scale_line = scale_line).first()
                        second_user_answer_scale = UserScaleAnswer.objects.filter(user=user_second,answer_scale_line = scale_line).first()
                        if first_user_answer_scale is not None and second_user_answer_scale is not None and first_user_answer_scale.answer == second_user_answer_scale.answer:
                            count_answers_line+=1
                    if count_answers_line == answer_scale_line_qu.count():
                        count_answers += 1
                for question_with_option in questions_with_option:
                    first_user_answer_option = UserOptionAnswer.objects.filter(user=user_first,question_with_option = question_with_option).first()
                    second_user_answer_option = UserOptionAnswer.objects.filter(user=user_second,question_with_option = question_with_option).first()
                    if first_user_answer_option is not None and second_user_answer_option is not None and first_user_answer_option.answer == second_user_answer_option.answer:
                        count_answers+=1
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A1')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A1')
                    )
                ).count() == 0 and user_second.gender != first_user_data.gender and count_answers >= (45 / 64) * len(
                    questions_with_option
                ) * len(
                    questions_with_scale
                ):
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A1')
                    count_match +=1
            print(f"Алгоритм 1 работает!")
            ok=True
            return ok,count_match
    except (CustomUser.DoesNotExist,QuestionWithOption.DoesNotExist,QuestionWithScale.DoesNotExist, ):
        print(f"Алгоритм 1 не работает(")
        ok=False
        count_match = -1
        return ok,count_match

# Второй алгоритм поиска партнеров

@app.task
def second_algorithm():
    try:
        users_all = CustomUser.objects.all().filter(test_status = 'finish')
        for user in users_all:
            user_first = user.id
            ok = graphene.Boolean()
            count_match = graphene.Int()
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                first_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_first,answer=1).count()
                second_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_second,answer=1).count()
                first_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_first,answer=5).count()
                second_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_second,answer=5).count()
                first_user_answer_scale_2 = UserScaleAnswer.objects.filter(user=user_first,answer=2).count()
                second_user_answer_scale_2 = UserScaleAnswer.objects.filter(user=user_second,answer=2).count()
                first_user_answer_scale_4 = UserScaleAnswer.objects.filter(user=user_first,answer=4).count()
                second_user_answer_scale_4 = UserScaleAnswer.objects.filter(user=user_second,answer=4).count()
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A2')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A2')
                    )
                ).count() == 0 and (((first_user_answer_scale_1==second_user_answer_scale_5)or(second_user_answer_scale_1==first_user_answer_scale_5))and((first_user_answer_scale_2==second_user_answer_scale_4)or(second_user_answer_scale_2==first_user_answer_scale_4))) and user_second.gender != first_user_data.gender:
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A2')
                    count_match +=1
            print(f"Алгоритм 2 работает!")
            ok=True
            return ok,count_match
    except (CustomUser.DoesNotExist,UserScaleAnswer.DoesNotExist, ):
        print(f"Алгоритм 2 не работает(")
        ok=False
        count_match = -1
        return ok,count_match

# Третий алгоритм поиска партнеров

@app.task
def third_algorithm():
    try:
        users_all = CustomUser.objects.all().filter(test_status = 'finish')
        for user in users_all:
            user_first = user.id
            ok = graphene.Boolean()
            count_match = graphene.Int()
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                first_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_first,answer=1).count()
                second_user_answer_scale_1 = UserScaleAnswer.objects.filter(user=user_second,answer=1).count()
                first_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_first,answer=5).count()
                second_user_answer_scale_5 = UserScaleAnswer.objects.filter(user=user_second,answer=5).count()
                if Datings.objects.all().filter(
                    (
                        Q(user_1=first_user_data)
                        & Q(user_2=user_second)
                        & Q(algorithm='A3')
                    )
                    | (
                        Q(user_1=user_second)
                        & Q(user_2=first_user_data)
                        & Q(algorithm='A3')
                    )
                ).count() == 0 and first_user_answer_scale_1>=35 and second_user_answer_scale_1>=35 and first_user_answer_scale_5>=5 and second_user_answer_scale_5>=5 and user_second.gender != first_user_data.gender:
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='A3')
                    count_match +=1
            print(f"Алгоритм 3 работает!")
            ok=True
            return ok,count_match
    except (CustomUser.DoesNotExist,UserScaleAnswer.DoesNotExist, ):
        print(f"Алгоритм 3 не работает(")
        ok=False
        count_match = -1
        return ok,count_match

# Четвертый алгоритм поиска партнеров

@app.task
def fourth_algorithm():
    try:
        users_all = CustomUser.objects.all().filter(test_status = 'finish')
        for user in users_all:
            user_first = user.id
            ok = graphene.Boolean()
            count_match = graphene.Int()
            first_user_data = CustomUser.objects.get(pk=user_first)
            users = CustomUser.objects.all().exclude(pk=user_first).filter(test_status = 'finish')
            count_match = 0
            for user_second in users:
                if (
                    (
                        first_user_data.number_foto_history_by_felling is not None
                        or user_second.number_foto_history_by_felling is not None
                    )
                    and user_second.gender != first_user_data.gender
                    and Datings.objects.all()
                    .filter(
                        (
                            Q(user_1=first_user_data)
                            & Q(user_2=user_second)
                            & Q(algorithm='HBF')
                        )
                        | (
                            Q(user_1=user_second)
                            & Q(user_2=first_user_data)
                            & Q(algorithm='HBF')
                        )
                    )
                    .count()
                    == 0
                    and first_user_data.number_foto_history_by_felling
                    == user_second.number_foto_history_by_felling
                ):
                    Datings.objects.create(user_1=first_user_data, user_2=user_second, algorithm='HBF')
                    count_match +=1
            print(f"Алгоритм 4 работает!")
            ok=True
            return ok,count_match
    except (CustomUser.DoesNotExist, ):
        print(f"Алгоритм 4 не работает(")
        ok=False
        count_match = -1
        return ok,count_match
