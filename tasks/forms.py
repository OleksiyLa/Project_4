from django import forms
from .models import Goal, Task, ScheduledTask

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
    class Meta:
        model = ScheduledTask
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduledTaskForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = False

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        date = cleaned_data.get('date')
        if start_time and end_time and start_time >= end_time:
            self.add_error('end_time', 'End time must be later than start time.')
        if date:
            tasks_on_date = ScheduledTask.objects.filter(date=date)
            if tasks_on_date.exists():
                for task in tasks_on_date:
                    if task == self.instance:
                        continue
                    elif(start_time >= task.start_time and start_time < task.end_time) or (end_time > task.start_time and end_time <= task.end_time):
                        self.add_error('start_time', 'Start time and end time cannot overlap with another task.')
                        break
