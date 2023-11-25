from django import forms
from datetime import datetime, timedelta
from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Goal, Task, ScheduledTask


class GoalForm(forms.ModelForm):
    """
    This is a form that helps to validate the data entered by the user
    when creating or editing a goal.
    It has a title field that is required and must be between 3 and 50
    characters long.
    It has a description field that is required and must be between 20
    and 2500 characters long.
    It has an expected_deadline field that is required and must be a
    date.
    """
    title = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a title'}),
        error_messages={'required': "Please enter a title."}
        )
    description = forms.CharField(
        min_length=20,
        max_length=2500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Describe your goal and how you will achieve it'}),
        error_messages={'required': "Please enter a description."}
        )
    expected_deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'}),
        error_messages={'required': "Please enter a deadline."}
    )

    class Meta:
        model = Goal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        user = cleaned_data.get('user')

        if title and user:
            existing_goals = Goal.objects.filter(title=title, user=user)
            if self.instance and self.instance.pk:
                existing_goals = existing_goals.exclude(pk=self.instance.pk)
            if existing_goals.exists():
                self.add_error('title',
                               "Goal with this Title and already exists.")

        return cleaned_data


class AddGoalForm(GoalForm):
    """
    This is a form that helps to validate the data entered by the user
    when creating a goal.
    It is an extension of the GoalForm class. It has a status field
    that is required and must be one of the choices from the STATUS
    list.
    """
    expected_deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': datetime.now().date}),
        error_messages={'required': "Please enter a deadline."}
    )

    def clean(self):
        cleaned_data = super().clean()
        expected_deadline = cleaned_data.get('expected_deadline')

        if expected_deadline and expected_deadline < datetime.today().date():
            self.add_error('expected_deadline',
                           'Estimation must be today or later.')

        return cleaned_data


class EditGoalForm(GoalForm):
    """
    This is a form that helps to validate the data entered by the user
    when editing a goal.
    It is an extension of the GoalForm class. It has a status field
    that is required and must be one of the choices from the STATUS
    list.
    """
    status = forms.ChoiceField(
        choices=Goal.STATUS,
        widget=forms.Select(attrs={'class': 'form-select w-100 p-2'}),
        error_messages={'required': "Please select a status."}
    )


class TaskForm(forms.ModelForm):
    """
    This is a form that helps to validate the data entered by the user
    when creating or editing a task.
    It has a title field that is required and must be between 3 and 50
    characters long.
    It has a description field that is required and must be between 20
    and 2500 characters long.
    """
    title = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a title'}),
        error_messages={'required': "Please enter a title."}
    )
    description = forms.CharField(
        min_length=20,
        max_length=2500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Describe your task that supports your goal'
            }),
        error_messages={'required': "Please enter a description."}
    )

    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['goal'].required = False

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        user = cleaned_data.get('user')

        if title and user:
            existing_tasks = Task.objects.filter(title=title, user=user)
            if self.instance and self.instance.pk:
                existing_tasks = existing_tasks.exclude(pk=self.instance.pk)
            if existing_tasks.exists():
                self.add_error('title',
                               "Task with this Title and already exists.")

        return cleaned_data


class ScheduledTaskForm(forms.ModelForm):
    """
    This is a form that helps to validate the data entered by the user
    when creating or editing a scheduled task.
    It has a start_time field that is required and must be a time.
    It has an end_time field that is required and must be a time.
    It has a date field that is required and must be a date.
    """
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter a start time."}
        )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter an end time."}
        )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter a date."}
        )

    class Meta:
        model = ScheduledTask
        fields = ['start_time', 'end_time', 'date']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            self.add_error(None,
                           'End time must be later than start time.')
        return cleaned_data


class AddScheduledTaskForm(ScheduledTaskForm):
    """
    This is a form that helps to validate the data entered by the user
    when creating a scheduled task.
    It is an extension of the ScheduledTaskForm class. It has an
    end_date field that is required and must be a date.
    It has a selected_days field that is required and must be a list
    of days of the week.
    """
    date = forms.DateField(
        label='Exact date or start date',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': datetime.now().date,
            'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter a date."}
        )
    end_date = forms.DateField(
        label='End date (Optional)',
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': datetime.now().date() + timedelta(days=1),
            'class': 'form-control pr-5'}),
        )
    selected_days = forms.MultipleChoiceField(
        choices=[
            ('0', 'Monday'),
            ('1', 'Tuesday'),
            ('2', 'Wednesday'),
            ('3', 'Thursday'),
            ('4', 'Friday'),
            ('5', 'Saturday'),
            ('6', 'Sunday'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta(ScheduledTaskForm.Meta):
        fields = ScheduledTaskForm.Meta.fields + ['end_date', 'selected_days']

    def clean(self):
        cleaned_data = super().clean()
        end_date = cleaned_data.get('end_date')
        selected_days = cleaned_data.get('selected_days')
        date = cleaned_data.get('date')

        if date and date < datetime.today().date():
            self.add_error('date', 'Date must be today or later.')

        if end_date and date:
            if end_date < date:
                self.add_error('end_date',
                               'End date should be after start date.')
            msg = "Don't choose an end date for a single-day schedule."
            if end_date == date:
                self.add_error('end_date', msg)
            if end_date <= datetime.today().date():
                self.add_error('end_date',
                               'End date should be in the future.')
            if not selected_days:
                self.add_error('selected_days',
                               'Please select at least one weekday.')
        return cleaned_data


class EditScheduledTaskForm(ScheduledTaskForm):
    """
    This is a form that helps to validate the data entered by the user
    when editing a scheduled task.
    It is an extension of the ScheduledTaskForm class. It has a
    completed field that is not required.
    """
    completed = forms.BooleanField(required=False)

    class Meta(ScheduledTaskForm.Meta):
        fields = ScheduledTaskForm.Meta.fields + ['completed']


class CustomLoginForm(LoginForm):
    """
    This is a form that helps to validate the data entered by the user
    when logging in.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))

        self.fields['login'].error_messages = {
            'required': 'Username is required',
        }

        self.fields['password'].error_messages = {
            'required': 'Password is required'
        }

        self.fields['password'].help_text = None


class CustomSignupForm(SignupForm):
    """
    This is a form that helps to validate the data entered by the user
    when signing up.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))

        self.fields['username'].error_messages = {
            'required': 'Username is required',
        }

        self.fields['password1'].error_messages = {
            'required': 'Password is required'
        }

        self.fields['password2'].error_messages = {
            'required': 'Password confirmation is required'
        }
