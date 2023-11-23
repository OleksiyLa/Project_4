from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class Goal(models.Model):
    """
    This class represents the goal model.
    It has a title, slug, user, description,
    created_at, updated_at, expected_deadline, status.
    It has a save method that saves the slug automatically.
    It has a task_count method that returns the number of tasks
    related to the goal.
    It has a all_tasks_done method that returns True if all tasks
    related to the goal are completed.
    It has a tasks_to_complete method that returns the number of
    tasks that are not completed.
    """
    STATUS = [
        ('0', "ToDo"),
        ('1', "In Progress"),
        ('2', "On Hold"),
        ('3', "Done"),
    ]
    title = models.CharField(
        max_length=50,
        null=False)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False)
    description = models.TextField(
        max_length=2500,
        null=False)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)
    expected_deadline = models.DateField()
    status = models.CharField(
        default='0',
        blank=True,
        max_length=1,
        choices=STATUS)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        current_timestamp = int(
            timezone.now().timestamp())
        self.slug = f"{slug}-{current_timestamp}"
        super(Goal, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def task_count(self):
        return self.tasks.filter(goal=self).count()

    def all_tasks_done(self):
        compl_count = self.tasks.filter(goal=self, completed=True).count()
        total_tasks_count = self.tasks.filter(goal=self).count()
        return compl_count == total_tasks_count and total_tasks_count != 0

    def tasks_to_complete(self):
        return self.tasks.filter(goal=self, completed=False).count()


class Task(models.Model):
    """
    This class represents the task model.
    It has a title, slug, user, description,
    goal, created_at, completed.
    It has a save method that saves the slug automatically.
    It has a scheduled_task_count method that returns the number of
    scheduled tasks related to the task.
    It has a completed_task_count method that returns the number of
    scheduled tasks related to the task that are completed.
    It has a not_completed_task_count method that returns the number of
    scheduled tasks related to the task that are not completed.
    It has a failed_task_count method that returns the number of
    scheduled tasks related to the task that are not completed and
    are past the deadline.
    """
    title = models.CharField(
        max_length=50,
        null=False)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False)
    description = models.TextField(
        max_length=2500,
        null=False)
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=False)
    created_at = models.DateTimeField(
        auto_now_add=True)
    completed = models.BooleanField(
        default=False,
        blank=True)

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

    def failed_task_count(self):
        return self.scheduled_dates.filter(
            completed=False,
            date__lt=timezone.now().date()).count()


class ScheduledTask(models.Model):
    """
    This class represents the scheduled task model.
    It has a task, slug, user, date, start_time, end_time, completed.
    It has a save method that saves the slug automatically.
    It has a is_date_past_goal_deadline method that returns True if
    the date of the scheduled task is past the deadline of the goal.
    """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='scheduled_dates',
        null=False,
        blank=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=True)
    date = models.DateField(
        null=False)
    start_time = models.TimeField(
        null=False)
    end_time = models.TimeField(
        null=False)
    completed = models.BooleanField(
        default=False,
        blank=True)

    class Meta:
        unique_together = ['date', 'start_time', 'end_time', 'user']

    def save(self, *args, **kwargs):
        slug_1 = slugify(self.date)
        slug_2 = slugify(self.start_time)
        slug_3 = slugify(self.end_time)
        slug_4 = slugify(self.user)
        self.slug = f"{slug_1}-{slug_2}-{slug_3}-{slug_4}"
        super(ScheduledTask, self).save(*args, **kwargs)

    def __str__(self):
        title = self.task.title
        date = self.date
        start_time = self.start_time
        end_time = self.end_time
        return f"{title}-{date}-{start_time}-{end_time}"

    def is_date_past_goal_deadline(self):
        return self.task.goal.expected_deadline < self.date
