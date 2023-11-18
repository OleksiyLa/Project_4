from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit
from .models import Goal, Task, ScheduledTask
from datetime import timedelta, datetime
from django.contrib.auth.models import User

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
    

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['goal'].required = False


class ScheduledTaskForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter a start time."}
        )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control pr-5'}),
        error_messages={'required': "Please enter an end time."}
        )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control pr-5'}),
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
            raise ValidationError('End time must be later than start time.')
        return cleaned_data


class AddScheduledTaskForm(ScheduledTaskForm):
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    selected_days = forms.MultipleChoiceField(
        label='Selected Days',
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
            raise ValidationError('Date must be today or later.')

        if end_date and date:
            if end_date < date:
                self.add_error('end_date', 'End date should be after start date.')
            if end_date == date:
                self.add_error('end_date', 'Do not select end date if you want to schedule for one day only.')
            if end_date <= datetime.today().date():
                self.add_error('end_date', 'End date should be in the future.')
            if not selected_days:
                self.add_error('selected_days', 'Please select at least one weekday.')
        return cleaned_data


class EditScheduledTaskForm(ScheduledTaskForm):
    completed = forms.BooleanField(required=False)

    class Meta(ScheduledTaskForm.Meta):
        fields = ScheduledTaskForm.Meta.fields + ['completed']
