from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse
import json
from datetime import date
from .forms import GoalForm, TaskForm, ScheduleForm, ScheduledDateForm
from .models import Goal, Task, Schedule, ScheduledDate


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
    if task is None:
        return redirect('goals_board')

    if request.method == 'POST':
        date_form = ScheduledDateForm(request.POST)
        if date_form.is_valid():
            schedule_form = ScheduleForm(request.POST)
            scheduled_date = date_form.save(commit=False)
            scheduled_date.save()

            schedule = schedule_form.save(commit=False)
            schedule.task = task
            schedule.save()
            schedule.scheduled_dates.add(scheduled_date)
            end_date = request.POST.get('end_date')
            end_date = date.fromisoformat(end_date)
            return redirect(reverse('tasks'))
    else:
        date_form = ScheduledDateForm()

    return render(request, 'schedule.html', {'date_form': date_form })

class CalendarView(TemplateView):
    template_name = 'calendar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'calendar'
        return context


def calendar_data(request):
    data = Schedule.objects.all()
    schedule_data = []

    for task in Task.objects.all():
        task_schedules = data.filter(task=task)

        if task_schedules.exists():
            schedule_list = [{"scheduled_dates": list(item.scheduled_dates.values())} for item in task_schedules]
            schedule_data.append({"task_title": task.title, "task_slug": task.slug, "url": reverse('delete_task', args=[task.slug]), "task_description": task.description, "schedule_list": schedule_list})

    response_data = schedule_data

    print(response_data)
    return JsonResponse(response_data, safe=False)
