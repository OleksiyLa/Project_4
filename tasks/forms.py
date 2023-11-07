from django import forms
from .models import Goal, Task, Schedule, ScheduledDate

class GoalForm(forms.ModelForm):
  class Meta:
    model = Goal
    fields = '__all__'

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['goal'].required = False

class ScheduledDateForm(forms.ModelForm):
    class Meta:
        model = ScheduledDate
        fields = '__all__'

class ScheduleForm(forms.ModelForm):
    scheduled_dates = forms.ModelMultipleChoiceField(
        queryset=ScheduledDate.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Schedule
        fields = ['task', 'scheduled_dates']

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = False
