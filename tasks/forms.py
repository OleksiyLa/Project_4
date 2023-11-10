from django import forms
from .models import Goal, Task, ScheduledTask

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


class ScheduledTaskForm(forms.ModelForm):
    class Meta:
        model = ScheduledTask
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduledTaskForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = False
