# Generated by Django 4.2.7 on 2023-11-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_scheduledtask_alter_scheduleddate_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledtask',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
