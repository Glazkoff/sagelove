# Generated by Django 3.2.5 on 2021-07-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_questionwithoption_published_or_not'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answeroption',
            name='answer_value',
        ),
    ]
