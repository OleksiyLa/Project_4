from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime
from .forms import GoalForm, TaskForm, ScheduledTaskForm
from .models import Goal, Task, ScheduledTask


# Create your views here.
class GoalsBoardView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'goals_board.html'
    context_object_name = 'goals'
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'goals'
        return context


class CreateGoalView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'create_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditGoalView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'edit_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def delete_goal(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.delete()
    return redirect(reverse('goals_board'))


@login_required
def add_task(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    if goal is None:
        return redirect('goals_board')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'goal': goal.id })


class TasksView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('goal__title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.filter(user=self.request.user).values_list('goal__title', 'goal__slug').distinct()
        context["goals"] = goals
        return context


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('goal__title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.values_list('goal__title', 'goal__slug').distinct()
        context["goals"] = goals
        return context


@login_required
def delete_task(request, slug):
    task = Task.objects.get(slug=slug, user=request.user)
    task.delete()
    return redirect(reverse('tasks'))


@login_required
def schedule_task(request, slug):
    task = Task.objects.get(slug=slug, user=request.user)
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
            validation_failed = False
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                if end_date <= start_date:
                    error_message = "End date should be later than start date."
                    form.errors['end_date'] = form.error_class([error_message])
                    return render(request, 'schedule.html', {'form': form, 'task': task.id})
                delta = timedelta(days=1)
                validatied_tasks = []
                while start_date <= end_date and not validation_failed:
                    if str(start_date.weekday()) in selected_days:
                        conflicting_tasks = ScheduledTask.objects.filter(
                            date=start_date,
                            start_time__lt=end_time,
                            end_time__gt=start_time,
                            user=request.user
                        )
                        if conflicting_tasks.exists():
                            error_message = 'Task overlaps with another scheduled task.'
                            form.add_error(None, error_message)
                            return render(request, 'schedule.html', {'form': form, 'task': task})
                        scheduled_task = ScheduledTask(
                            task=task, date=start_date, start_time=start_time, end_time=end_time, user=request.user
                        )
                        try:
                            scheduled_task.full_clean()
                            validatied_tasks.append(scheduled_task)
                        except ValidationError as e:
                            form.add_error(None, e)
                            validation_failed = True
                    start_date += delta
                if validation_failed:
                    return render(request, 'schedule.html', {'form': form, 'task': task.id})
                try:
                    for task in validatied_tasks:
                        task.save()
                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html', {'form': form, 'task': task.id})
            else:
                scheduled_task = ScheduledTask(
                    task=task, date=start_date, start_time=start_time, end_time=end_time, user=request.user
                )
                conflicting_tasks = ScheduledTask.objects.filter(
                    date=start_date,
                    start_time__lt=end_time,
                    end_time__gt=start_time,
                    user=request.user
                )
                if conflicting_tasks.exists():
                    print(conflicting_tasks)
                    error_message = 'Task overlaps with another scheduled task.'
                    form.add_error(None, error_message)
                    return render(request, 'schedule.html', {'form': form, 'task': task})
                try:
                    scheduled_task.full_clean()
                    scheduled_task.save()
                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html', {'form': form, 'task': task.id})
            return redirect(reverse('tasks'))
        else:
            return render(request, 'schedule.html', {'form': form, 'task': task.id})
    else:
        form = ScheduledTaskForm()
        return render(request, 'schedule.html', {'form': form, 'task': task.id})


class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'calendar.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'calendar'
        return context


@login_required
def calendar_data(request):
    all_tasks = Task.objects.filter(user=request.user)
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
                    "completed": item.completed,
                    "slug": item.slug,
                })
            schedule_data.append({
                "title": task.title,
                "slug": task.slug,
                "description": task.description,
                "schedule": schedule_list
            })
    return JsonResponse(schedule_data, safe=False)


@login_required
def delete_scheduled_task(request, slug):
    scheduled_task = ScheduledTask.objects.get(slug=slug, user=request.user)
    scheduled_task.delete()
    response = HttpResponseRedirect('/calendar/')
    response.set_cookie('selectedDate', slug, max_age=300)
    return response


@login_required
def edit_scheduled_task(request, slug):
    scheduled_task = ScheduledTask.objects.get(slug=slug, user=request.user)
    
    if request.method == 'POST':
        form = ScheduledTaskForm(request.POST, instance=scheduled_task)
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect('/calendar/')
            response.set_cookie('selectedDate', slug, max_age=300)
            return response
    else:
        form = ScheduledTaskForm(instance=scheduled_task)
        
    return render(request, 'edit_scheduled_task.html', {'form': form, 'task': scheduled_task.task })


@login_required
def complete_scheduled_task(request, slug):
    scheduled_task = ScheduledTask.objects.get(slug=slug, user=request.user)
    scheduled_task.completed = True
    scheduled_task.save()
    response = HttpResponseRedirect('/calendar/')
    response.set_cookie('selectedDate', slug, max_age=300)
    return response
