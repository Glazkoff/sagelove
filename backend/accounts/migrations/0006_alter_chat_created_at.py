# Generated by Django 3.2.6 on 2021-08-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_chat_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создание чата'),
        ),
    ]
