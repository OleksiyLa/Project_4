from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import timedelta, datetime
from .forms import TaskForm, AddScheduledTaskForm, EditScheduledTaskForm, AddGoalForm, EditGoalForm
from .models import Goal, Task, ScheduledTask


# Create your views here.
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

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
    form_class = AddGoalForm
    template_name = 'create_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Goal created successfully!')
        return super().form_valid(form)


class EditGoalView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = EditGoalForm
    template_name = 'edit_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Goal updated successfully!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No goal found")
        if not obj.user == self.request.user:
            raise Http404("No goal found")
        return obj
    
@login_required
def select_progress_status(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '1'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))

@login_required
def select_on_hold_status(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '2'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))

@login_required
def select_done_status(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '3'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))

@login_required
def delete_goal(request, slug):
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.delete()
    messages.success(request, 'Goal deleted successfully!')
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
            messages.success(request, 'Task added successfully')
            return redirect('tasks')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form, 'goal': goal.id, 'goal_title': goal.title.capitalize() })


class TasksView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('goal__title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.filter(user=self.request.user).values_list('goal__title', 'goal__slug', 'goal__id').distinct()
        context["goals"] = goals
        return context


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        task = self.get_object()
        context["goal_id"] = task.goal.pk
        context["goal_title"] = task.goal.title
        return context
    
    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()   
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No task found")
        if not obj.user == self.request.user:
            raise Http404("No task found")
        return obj


@login_required
def delete_task(request, slug):
    task = Task.objects.get(slug=slug, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect(reverse('tasks'))


@login_required
def schedule_task(request, slug):
    task = Task.objects.get(slug=slug, user=request.user)
    task_title = task.title.capitalize()
    if not task:
        return redirect('tasks')
    
    if request.method == 'POST':
        form = AddScheduledTaskForm(request.POST)
        if form.is_valid():
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            date = request.POST.get('date')
            end_date = request.POST.get('end_date')
            selected_days = request.POST.getlist('selected_days')
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
                print(selected_days)
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
                            return render(request, 'schedule.html', {'form': form, 'task': task, 'task_title': task_title})
                        scheduled_task = ScheduledTask(
                            task=task, date=start_date, start_time=start_time, end_time=end_time, user=request.user
                        )
                        validatied_tasks.append(scheduled_task)
                    start_date += delta
                if validation_failed:
                    return render(request, 'schedule.html', {'form': form, 'task': task.id, 'task_title': task_title})
                try:
                    num_of_past_deadline = 0
                    for task in validatied_tasks:
                        task.save()
                        if(task.is_date_past_goal_deadline()):
                            num_of_past_deadline += 1
                    num_of_scheduled_tasks = len(validatied_tasks)
                    if num_of_past_deadline > 0:
                        messages.warning(request, f'{num_of_scheduled_tasks} tasks scheduled successfully, but {num_of_past_deadline} of them are past the goal deadline.')
                    else:
                        messages.success(request, f'{num_of_scheduled_tasks} tasks scheduled successfully!')
                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html', {'form': form, 'task': task.id, 'task_title': task_title})
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
                    error_message = 'Task overlaps with another scheduled task.'
                    form.add_error(None, error_message)
                    return render(request, 'schedule.html', {'form': form, 'task': task, 'task_title': task_title})
                try:
                    scheduled_task.save()
                    if(scheduled_task.is_date_past_goal_deadline()):
                        messages.warning(request, 'Task scheduled successfully, but the date is past the goal deadline.')
                    else:
                        messages.success(request, 'Task scheduled successfully!')

                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html', {'form': form, 'task': task.id, 'task_title': task_title})
            return redirect(reverse('tasks'))
        else:
            return render(request, 'schedule.html', {'form': form, 'task': task.id, 'task_title': task_title})
    else:
        form = AddScheduledTaskForm()
        return render(request, 'schedule.html', {'form': form, 'task': task.id, 'task_title': task_title})


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
    messages.success(request, 'Scheduled task deleted successfully!')
    return response


@login_required
def edit_scheduled_task(request, slug):
    scheduled_task = ScheduledTask.objects.get(slug=slug, user=request.user)
    if request.method == 'POST':
        form = EditScheduledTaskForm(request.POST, instance=scheduled_task)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            date = form.cleaned_data['date']
            conflicting_tasks = ScheduledTask.objects.filter(
                ~Q(pk=scheduled_task.pk),
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time,
                user=request.user
            )
            if conflicting_tasks.exists():
                error_message = 'Task overlaps with another scheduled task.'
                form.add_error(None, error_message)
            else:
                scheduled_task.start_time = start_time
                scheduled_task.end_time = end_time
                scheduled_task.date = date
                scheduled_task.completed = form.cleaned_data['completed']
                scheduled_task.save()
                response = HttpResponseRedirect('/calendar/')
                response.set_cookie('selectedDate', slug, max_age=300)
                messages.success(request, 'Scheduled task updated successfully!')
                return response
    else:
        form = EditScheduledTaskForm(instance=scheduled_task)
    return render(request, 'edit_scheduled_task.html', {'form': form, 'task_title': scheduled_task.task.title.capitalize() })


@login_required
def complete_scheduled_task(request, slug):
    scheduled_task = ScheduledTask.objects.get(slug=slug, user=request.user)
    scheduled_task.completed = True
    scheduled_task.save()
    response = HttpResponseRedirect('/calendar/')
    response.set_cookie('selectedDate', slug, max_age=300)
    messages.success(request, 'Scheduled task completed successfully!')
    return response
