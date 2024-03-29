# Generated by Django 5.0.1 on 2024-01-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Task name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Task description')),
                ('due_date', models.DateTimeField(verbose_name='Date and time when task is done')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
            },
        ),
    ]
