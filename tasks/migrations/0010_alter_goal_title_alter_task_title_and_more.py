# Generated by Django 4.2.7 on 2023-11-20 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_remove_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='goal',
            unique_together={('title', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='scheduledtask',
            unique_together={('date', 'start_time', 'end_time', 'user', 'task')},
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('title', 'user')},
        ),
    ]
