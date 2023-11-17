from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML
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
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    completed = forms.BooleanField(required=False)

    class Meta:
        model = ScheduledTask
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'required': 'required'}),
            'start_time': forms.TimeInput(attrs={'required': 'required'}),
            'end_time': forms.TimeInput(attrs={'required': 'required'}),
        }
        error_messages = {
            'date': {'required': "Please enter a date."},
            'start_time': {'required': "Please enter a start time."},
            'end_time': {'required': "Please enter an end time."},
        }

    def __init__(self, *args, **kwargs):
        super(ScheduledTaskForm, self).__init__(*args, **kwargs)
        self.fields['task'].required = False
        self.fields['date'].required = True
        self.fields['start_time'].required = True
        self.fields['end_time'].required = True

        # Crispy Forms integration
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('start_time', css_class='form-control p-2'),
                    css_class='mr-2'
                ),
                Div(
                    Field('end_time', css_class='form-control p-2'),
                    css_class='mr-2'
                ),
                css_class='mb-3 d-flex justify-content-around'
            ),
            Div(
                HTML('<label for="{{ form.date.id_for_label }}" class="form-label d-block text-center lead">Exact date:</label>'),
                Field('date', css_class='form-control w-100 p-2'),
                css_class='mb-4'
            ),
            Div(
                Field('completed', css_class='p-3'),
                css_class='mb-4'
            ),
        )