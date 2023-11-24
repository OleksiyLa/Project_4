from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import timedelta, datetime
from allauth.account.views import LoginView, SignupView
import tasks.forms as myFormModels
from .models import Goal, Task, ScheduledTask


# Create your views here.
def custom_404_view(request, exception):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)


class GoalsBoardView(LoginRequiredMixin, ListView):
    """View for the goals board."""
    model = Goal
    template_name = 'goals_board.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'goals'
        return context


class GoalDetailView(LoginRequiredMixin, DetailView):
    """View for the goal details."""
    model = Goal
    template_name = 'goal_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("Not found")
        if not obj.user == self.request.user:
            raise Http404("Not found")
        return obj


class CreateGoalView(LoginRequiredMixin, CreateView):
    """View for creating a goal."""
    model = Goal
    form_class = myFormModels.AddGoalForm
    template_name = 'create_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Goal created successfully!')
        return super().form_valid(form)


class EditGoalView(LoginRequiredMixin, UpdateView):
    """
    View for editing a goal.
    edit_goal_url is used in the template
    to redirect back to the goals board page.
    """
    model = Goal
    form_class = myFormModels.EditGoalForm
    template_name = 'edit_goal.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,
                         'Goal updated successfully!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No goal found")
        if not obj.user == self.request.user:
            raise Http404("No goal found")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_goal_url"] = 'goals_board'
        return context


class EditGoalViewFromDetails(LoginRequiredMixin, UpdateView):
    """
    View for editing a goal.
    This view is used when editing a goal from the goal details page
    and redirects to the goal details page after editing the goal.
    edit_goal_url is used in the template
    to redirect back to the goal details page.
    """
    model = Goal
    form_class = myFormModels.EditGoalForm
    template_name = 'edit_goal.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,
                         'Goal updated successfully!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No goal found")
        if not obj.user == self.request.user:
            raise Http404("No goal found")
        return obj

    def get_success_url(self):
        return reverse('goal_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_goal_url"] = 'goal_detail'
        context["slug"] = self.object.slug
        return context


@login_required
def select_progress_status(request, slug):
    """View for selecting the progress status of a goal."""
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '1'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))


@login_required
def select_on_hold_status(request, slug):
    """View for selecting the on hold status of a goal."""
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '2'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))


@login_required
def select_done_status(request, slug):
    """View for selecting the done status of a goal."""
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.status = '3'
    goal.save()
    messages.success(request, 'Goal status updated successfully!')
    return redirect(reverse('goals_board'))


@login_required
def delete_goal(request, slug):
    """View for deleting a goal."""
    goal = Goal.objects.get(slug=slug, user=request.user)
    goal.delete()
    messages.success(request, 'Goal deleted successfully!')
    return redirect(reverse('goals_board'))


@login_required
def add_task(request, slug):
    """
    View for adding a task.
    Redirects to the goals board page after adding a task.
    """
    goal = Goal.objects.get(slug=slug, user=request.user)
    if goal is None:
        return redirect('goals_board')

    if request.method == 'POST':
        form = myFormModels.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
            return redirect('tasks')
    else:
        form = myFormModels.TaskForm()

    return render(request, 'add_task.html',
                  {'form': form,
                   'goal': goal.id,
                   'goal_title': goal.title.capitalize(),
                   'add_task_url': 'goals_board'})


@login_required
def add_task_from_tasks(request, slug):
    """
    View for adding a task. Redirects to the tasks page after adding a task.
    Actions in this view are almost the same as the add_task view,
    except for the redirect and the add_task_url.
    """
    goal = Goal.objects.get(slug=slug, user=request.user)
    if goal is None:
        return redirect('tasks')

    if request.method == 'POST':
        form = myFormModels.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
            return redirect('tasks')
    else:
        form = myFormModels.TaskForm()

    return render(request, 'add_task.html',
                  {'form': form,
                   'goal': goal.id,
                   'goal_title': goal.title.capitalize(),
                   'add_task_url': 'tasks'})


class TasksView(LoginRequiredMixin, ListView):
    """
    View for the tasks page. Displays all the tasks of the user.
    """
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        goals = Task.objects.filter(
            user=self.request.user).values_list(
                'goal__title', 'goal__slug', 'goal__id'
                ).distinct()
        context["goals"] = goals
        return context

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        ).order_by(
            'goal__title',
            'completed',
            'created_at'
        )


class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    View for the task details.
    Displays the details of a task.
    """
    model = Task
    template_name = 'task_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("Not found")
        if not obj.user == self.request.user:
            raise Http404("Not found")
        return obj


@login_required
def complete_task(request, slug):
    """
    View for completing a task.
    Redirects to the tasks page after completing a task.
    """
    task = Task.objects.get(slug=slug, user=request.user)
    task.completed = True
    task.save()
    response = HttpResponseRedirect('/tasks/')
    messages.success(request, 'Task completed successfully!')
    return response


@login_required
def uncomplete_task(request, slug):
    """
    View for uncompleting a task.
    Redirects to the tasks page after uncompleting a task.
    """
    task = Task.objects.get(slug=slug, user=request.user)
    task.completed = False
    task.save()
    response = HttpResponseRedirect('/tasks/')
    messages.success(request,
                     'Task is not completed now, success!')
    return response


class EditTaskView(LoginRequiredMixin, UpdateView):
    """
    View for editing a task.
    edit_task_url is used in the template
    to redirect back to the tasks page.
    """
    model = Task
    form_class = myFormModels.TaskForm
    template_name = 'edit_task.html'
    success_url = '/tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        task = self.get_object()
        context["goal_id"] = task.goal.pk
        context["goal_title"] = task.goal.title
        context["edit_task_url"] = 'tasks'
        return context

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        messages.success(self.request,
                         'Task updated successfully!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No task found")
        if not obj.user == self.request.user:
            raise Http404("No task found")
        return obj


class EditTaskViewFromDetails(LoginRequiredMixin, UpdateView):
    """
    View for editing a task.
    This view is used when editing
    a task from the task details page
    and redirects to the task details
    page after editing the task.
    """
    model = Task
    form_class = myFormModels.TaskForm
    template_name = 'edit_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'tasks'
        task = self.get_object()
        context["goal_id"] = task.goal.pk
        context["goal_title"] = task.goal.title
        context["edit_task_url"] = 'task_detail'
        context["slug"] = self.object.slug
        return context

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        messages.success(self.request,
                         'Task updated successfully!')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj:
            raise Http404("No task found")
        if not obj.user == self.request.user:
            raise Http404("No task found")
        return obj

    def get_success_url(self):
        return reverse('task_detail',
                       kwargs={'slug': self.object.slug})


@login_required
def delete_task(request, slug):
    """
    View for deleting a task.
    Redirects to the tasks page after deleting a task.
    """
    task = Task.objects.get(slug=slug, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect(reverse('tasks'))


@login_required
def schedule_task(request, slug):
    """
    View for scheduling a task.
    Redirects to the calendar page
    after scheduling a task.
    Creates one task if the end date is not specified.
    Tasks can be scheduled within a specified
    time frame when an end date is selected.
    Within the specified time range,
    tasks will be scheduled on the selected days of the week.
    The validation is included.
    If the task overlaps with another scheduled task,
    the task will not be scheduled.
    The maximum number of tasks that can be scheduled is 365,
    representing the maximum time range available.
    """
    task = Task.objects.get(slug=slug, user=request.user)
    task_title = task.title.capitalize()
    if not task:
        return redirect('tasks')

    if request.method == 'POST':
        form = myFormModels.AddScheduledTaskForm(request.POST)
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
                days_schedlued = (end_date - start_date).days + 1
                if (days_schedlued > 365):
                    error_message = "Scheduling is limited to 365 days."
                    form.errors['end_date'] = form.error_class([error_message])
                    return render(request,
                                  'schedule.html',
                                  {'form': form,
                                   'task': task.id,
                                   'task_title': task_title})
                if end_date <= start_date:
                    error_message = "End date should be later than start date."
                    form.errors['end_date'] = form.error_class([error_message])
                    return render(request, 'schedule.html',
                                  {'form': form,
                                   'task': task.id,
                                   'task_title': task_title})
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
                            error_message = 'Task overlaps with another task.'
                            form.add_error(None, error_message)
                            return render(request, 'schedule.html',
                                          {'form': form,
                                           'task': task,
                                           'task_title': task_title})
                        scheduled_task = ScheduledTask(
                            task=task,
                            date=start_date,
                            start_time=start_time,
                            end_time=end_time,
                            user=request.user
                        )
                        validatied_tasks.append(scheduled_task)
                    start_date += delta
                if validation_failed:
                    return render(request, 'schedule.html',
                                  {'form': form,
                                   'task': task.id,
                                   'task_title': task_title})
                try:
                    past_deadline = 0
                    for task in validatied_tasks:
                        task.save()
                        if (task.is_date_past_goal_deadline()):
                            past_deadline += 1
                    num_of_tasks = len(validatied_tasks)
                    err_msg_1 = f'{num_of_tasks}tasks scheduled successfully'
                    err_msg_2 = f'{past_deadline} of them are past the goal'
                    if past_deadline > 0:
                        messages.warning(
                            request,
                            f'{err_msg_1}, but {err_msg_2} deadline.')
                    else:
                        messages.success(request, f'{msg}!')
                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html',
                                  {'form': form,
                                   'task': task.id,
                                   'task_title': task_title})
            else:
                scheduled_task = ScheduledTask(
                    task=task,
                    date=start_date,
                    start_time=start_time,
                    end_time=end_time,
                    user=request.user
                )
                conflicting_tasks = ScheduledTask.objects.filter(
                    date=start_date,
                    start_time__lt=end_time,
                    end_time__gt=start_time,
                    user=request.user
                )
                if conflicting_tasks.exists():
                    error_message = 'Task overlaps with another task.'
                    form.add_error(None, error_message)
                    return render(request, 'schedule.html',
                                  {'form': form,
                                   'task': task,
                                   'task_title': task_title})
                try:
                    scheduled_task.save()
                    msg = 'Task scheduled successfully'
                    if (scheduled_task.is_date_past_goal_deadline()):
                        messages.warning(
                            request,
                            {msg},
                            'but the date is past the goal deadline.')
                    else:
                        messages.success(request, f'{msg}!')

                except ValidationError as e:
                    form.add_error(None, e)
                    return render(request, 'schedule.html',
                                  {'form': form,
                                   'task': task.id,
                                   'task_title': task_title})
            return redirect(reverse('calendar'))
        else:
            return render(request, 'schedule.html',
                          {'form': form,
                           'task': task.id,
                           'task_title': task_title})
    else:
        form = myFormModels.AddScheduledTaskForm()
        return render(request, 'schedule.html',
                      {'form': form,
                       'task': task.id,
                       'task_title': task_title})


class CalendarView(LoginRequiredMixin, TemplateView):
    """View for the calendar page."""
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'calendar'
        return context


@login_required
def calendar_data(request):
    """
    View for sending the calendar data.
    Returns a JSON response.
    """
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
    """
    View for deleting a scheduled task.
    The task deleted is the one selected in the calendar.
    """
    scheduled_task = ScheduledTask.objects.get(slug=slug,
                                               user=request.user)
    scheduled_task.delete()
    response = HttpResponseRedirect('/calendar/')
    response.set_cookie('selectedDate', slug, max_age=300)
    messages.success(request, 'Scheduled task deleted successfully!')
    return response


@login_required
def edit_scheduled_task(request, slug):
    """
    View for editing a scheduled task.
    The task edited is the one selected in the calendar.
    """
    scheduled_task = ScheduledTask.objects.get(
        slug=slug, user=request.user)
    if request.method == 'POST':
        form = myFormModels.EditScheduledTaskForm(
            request.POST, instance=scheduled_task)
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
                messages.success(request,
                                 'Scheduled task updated successfully!')
                return response
    else:
        form = myFormModels.EditScheduledTaskForm(instance=scheduled_task)
    return render(request, 'edit_scheduled_task.html',
                  {'form': form,
                   'task_title': scheduled_task.task.title.capitalize()})


@login_required
def complete_scheduled_task(request, slug):
    """
    View for completing a scheduled task.
    The task completed is the one selected in the calendar.
    """
    scheduled_task = ScheduledTask.objects.get(slug=slug,
                                               user=request.user)
    scheduled_task.completed = True
    scheduled_task.save()
    response = HttpResponseRedirect('/calendar/')
    response.set_cookie('selectedDate', slug, max_age=300)
    messages.success(request, 'Scheduled task completed successfully!')
    return response


class CustomLoginView(LoginView):
    """Custom login view."""
    form_class = myFormModels.CustomLoginForm


class CustomSignupView(SignupView):
    """Custom signup view."""
    form_class = myFormModels.CustomSignupForm
