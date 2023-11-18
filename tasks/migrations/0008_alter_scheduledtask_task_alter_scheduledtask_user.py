# Generated by Django 4.2.7 on 2023-11-17 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_scheduledtask_user_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledtask',
            name='task',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_dates', to='tasks.task'),
        ),
        migrations.AlterField(
            model_name='scheduledtask',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
