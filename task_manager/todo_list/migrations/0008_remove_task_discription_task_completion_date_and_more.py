# Generated by Django 4.0 on 2022-02-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0007_alter_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='discription',
        ),
        migrations.AddField(
            model_name='task',
            name='completion_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
