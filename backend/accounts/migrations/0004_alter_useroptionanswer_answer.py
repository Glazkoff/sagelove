# Generated by Django 3.2.5 on 2021-07-09 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('accounts', '0003_auto_20210709_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroptionanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answeroption', verbose_name='Значение ответа'),
        ),
    ]
