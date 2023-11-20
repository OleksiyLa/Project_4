from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Goal(models.Model):
    STATUS = [
        ('0', "ToDo"),
        ('1', "In Progress"),
        ('2', "On Hold"),
        ('3', "Done"),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_deadline = models.DateField()
    status = models.CharField(default='0', blank=True, max_length=1, choices=STATUS)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        current_timestamp = int(timezone.now().timestamp())
        self.slug = f"{slug}-{current_timestamp}"
        super(Goal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def task_count(self):
        return Task.objects.filter(goal=self).count()


class Task(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True)
    
    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        current_timestamp = int(timezone.now().timestamp())
        self.slug = f"{slug}-{current_timestamp}"
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def scheduled_task_count(self):
        return self.scheduled_dates.count()

    def completed_task_count(self):
        return self.scheduled_dates.filter(completed=True).count()

    def not_completed_task_count(self):
        return self.scheduled_dates.filter(completed=False).count()


class ScheduledTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='scheduled_dates', null=False, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    completed = models.BooleanField(default=False, blank=True)

    class Meta:
        unique_together = ['date', 'start_time', 'end_time', 'user']
    
    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.date)}-{slugify(self.start_time)}-{slugify(self.end_time)}-{slugify(self.user)}"
        super(ScheduledTask, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.task.title} - {self.date} {self.start_time} - {self.end_time}"
    
    def is_date_past_goal_deadline(self):
        return self.task.goal.expected_deadline < self.date
