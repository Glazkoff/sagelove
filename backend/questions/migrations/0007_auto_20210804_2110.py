# Generated by Django 3.2.6 on 2021-08-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20210716_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionwithoption',
            name='published_or_not',
        ),
        migrations.RemoveField(
            model_name='questionwithscale',
            name='published_or_not',
        ),
        migrations.AddField(
            model_name='groupquestion',
            name='published_or_not',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
    ]
