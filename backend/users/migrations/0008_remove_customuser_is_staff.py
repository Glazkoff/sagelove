# Generated by Django 3.2.4 on 2021-06-23 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
    ]