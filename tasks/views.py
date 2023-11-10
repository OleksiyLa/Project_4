from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse
import json
from datetime import date, timedelta, datetime
from .forms import GoalForm, TaskForm, ScheduledTaskForm
from .models import Goal, Task, ScheduledTask


# Create your views here.
class GoalsBoardView(ListView):
    model = Goal
    template_name = 'goals_board.html'
    context_object_name = 'goals'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'goals'
        return context


class CreateGoalView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'create_goal.html'
    success_url = '/'


class EditGoalView(UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'edit_goal.html'
    success_url = '/'


def delete_goal(request, slug):
    goal = Goal.objects.get(slug=slug)
    goal.delete()
    return redirect(reverse('goals_board'))


def add_task(request, slug):
    goal = Goal.objects.get(slug=slug)
    if goal is None:
        return redirect('goals_board')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'goal': goal.id })


class TasksView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('goal__title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.values_list('goal__title', 'goal__slug').distinct()
        context["goals"] = goals
        return context


class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.values_list('goal__title', 'goal__slug').distinct()
        context["goals"] = goals
        return context


def delete_task(request, slug):
    task = Task.objects.get(slug=slug)
    task.delete()
    print(reverse('delete_task', args=[slug]))
    return redirect(reverse('tasks'))


def schedule_task(request, slug):
    task = Task.objects.get(slug=slug)
    if not task:
        return redirect('tasks')
    if request.method == 'POST':
        form = ScheduledTaskForm(request.POST)
        if form.is_valid():
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            date = request.POST.get('date')
            end_date = request.POST.get('end_date')
            selected_days = request.POST.getlist('selectedDays[]')
            start_date = datetime.strptime(date, "%Y-%m-%d").date()
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                delta = timedelta(days=1)
                while start_date <= end_date:
                    if str(start_date.weekday()) in selected_days:
                        ScheduledTask.objects.get_or_create(
                            task=task, date=start_date, start_time=start_time, end_time=end_time
                        )
                    start_date += delta
            else:
                ScheduledTask.objects.get_or_create(
                    task=task, date=start_date, start_time=start_time, end_time=end_time
                )
            return redirect(reverse('tasks'))
        else:
            return render(request, 'schedule.html', {'form': form, 'task': task.id})
    else:
        form = ScheduledTaskForm()
        return render(request, 'schedule.html', {'form': form, 'task': task.id})


class CalendarView(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'calendar'
        return context


def calendar_data(request):
    all_tasks = Task.objects.all()
    schedule_data = []

    for task in all_tasks:
        task_schedules = ScheduledTask.objects.filter(task=task)
        if task_schedules.exists():
            schedule_list = []
            for item in task_schedules:
                schedule_list.append({
                    "date": item.date,
                    "start_time": item.start_time,
                    "end_time": item.end_time,
                    "completed": item.completed
                })
            schedule_data.append({
                "title": task.title,
                "slug": task.slug,
                "url": reverse('delete_task', args=[task.slug]),
                "description": task.description,
                "schedule": schedule_list
            })
    return JsonResponse(schedule_data, safe=False)
