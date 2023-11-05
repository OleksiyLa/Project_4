from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse
from .forms import GoalForm
from .models import Goal

# Create your views here.
class GoalsBoardView(ListView):
    model = Goal
    template_name = 'goals_board.html'
    context_object_name = 'goals'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_link"] = 'goals'
        return context


class CreateGoalView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'create_goal.html'
    success_url = '/'


def delete_goal(request, slug):
    goal = Goal.objects.get(slug=slug)
    goal.delete()
    return redirect(reverse('goals_board'))
