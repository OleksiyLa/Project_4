from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from .forms import GoalForm, TaskForm
from .models import Goal, Task

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
    return redirect(reverse('tasks'))