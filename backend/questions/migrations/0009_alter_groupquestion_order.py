# Generated by Django 3.2.6 on 2021-08-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_groupquestion_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupquestion',
            name='order',
            field=models.IntegerField(verbose_name='Порядок'),
        ),
    ]
