from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoalsBoardView.as_view(), name='goals_board'),
    path('create_goal/', views.CreateGoalView.as_view(), name='create_goal'),
]
