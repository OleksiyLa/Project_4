from django.contrib import admin
from .models import Goal, Task, ScheduledTask


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    """
    This class is used to customize the admin interface for the Goal model.
    It has a list_display attribute that displays the title, created_at,
    updated_at, expected_deadline, and status fields in the admin interface.
    It has a list_filter attribute that filters the goals by status,
    created_at, and updated_at.
    It has a search_fields attribute that allows the admin to search
    for goals by title and description.
    It has a prepopulated_fields attribute that automatically fills the slug
    field based on the title field.
    """
    list_display = ('title', 'created_at', 'updated_at',
                    'expected_deadline', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    This class is used to customize the admin interface for the Task model.
    It has a list_display attribute that displays the title, created_at,
    and completed fields in the admin interface.
    It has a list_filter attribute that filters the tasks by created_at
    and completed.
    It has a search_fields attribute that allows the admin to search
    for tasks by title and description.
    It has a prepopulated_fields attribute that automatically fills the slug
    field based on the title field.
    """
    list_display = ('title', 'created_at', 'completed')
    list_filter = ('created_at', 'completed')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ScheduledTask)
