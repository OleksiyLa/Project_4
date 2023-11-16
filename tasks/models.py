from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError
# Create your models here.


class Goal(models.Model):
    STATUS = [
        ('0', "ToDo"),
        ('1', "In Progress"),
        ('2', "On Hold"),
        ('3', "Done"),
    ]
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_deadline = models.DateField()
    status = models.CharField(default='0', blank=True, max_length=1, choices=STATUS)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Goal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ScheduledTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='scheduled_dates')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        unique_together = ['date', 'start_time', 'end_time']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.date)}-{slugify(self.start_time)}-{slugify(self.end_time)}"
        super(ScheduledTask, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.task.title} - {self.date} {self.start_time} - {self.end_time}"

    def clean(self):
        if self.start_time and self.end_time and self.start_time >= self.end_time:
            raise ValidationError('End time must be later than start time.')

        if self.date:
            tasks_on_date = ScheduledTask.objects.filter(date=self.date)
            if self.pk:
                tasks_on_date = tasks_on_date.exclude(pk=self.pk)
            for task in tasks_on_date:
                if self.check_task_overlap(task):
                    raise ValidationError('Task overlaps with another scheduled task.')

    def check_task_overlap(self, other_task):
        return (
            (self.start_time < other_task.end_time) and
            (self.end_time > other_task.start_time)
        )