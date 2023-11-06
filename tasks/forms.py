from django import forms
from .models import Goal, Task

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
