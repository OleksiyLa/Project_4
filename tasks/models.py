from django.db import models

# Create your models here.


class Goal(models.Model):
    STATUS = [
        ('0', "ToDo"),
        ('1', "In Progress"),
        ('2', "On Hold"),
        ('3', "Done"),
    ]
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_deadline = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    scheduled_dates = models.ManyToManyField('ScheduledDate')

    def num_of_scheduled_dates(self):
        return self.scheduled_dates.count()

    def __str__(self):
        return self.task.title


class ScheduledDate(models.Model):
    date = models.DateField()
    scheduled_time = models.TimeField()

    class Meta:
        unique_together = ['date', 'scheduled_time']

    def __str__(self):
        return f"{self.date} {self.scheduled_time}"
