from django.contrib import admin
from .models import Goal, Task, ScheduledTask


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',
                    'expected_deadline', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'completed')
    list_filter = ('created_at', 'completed')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ScheduledTask)
