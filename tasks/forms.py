from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
  class Meta:
    model = Goal
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoalForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter the goal title'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe the goal'
        self.fields['deadline'].widget.attrs['placeholder'] = 'Select the deadline'
