# Generated by Django 4.0 on 2022-02-24 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0009_task_in_progresss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='in_progresss',
            new_name='in_progress',
        ),
    ]
