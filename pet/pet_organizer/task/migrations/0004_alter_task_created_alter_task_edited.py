# Generated by Django 5.0.1 on 2024-01-22 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_created_task_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 4, 5, 574927)),
        ),
        migrations.AlterField(
            model_name='task',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 15, 4, 5, 574927)),
        ),
    ]
