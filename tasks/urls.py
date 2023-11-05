from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoalsBoardView.as_view(), name='goals_board'),
    path('create_goal/', views.CreateGoalView.as_view(), name='create_goal'),
    path('delete_goal/<slug:slug>/', views.delete_goal, name='delete_goal'),
    path('edit_goal/<slug:slug>/', views.EditGoalView.as_view(), name='edit_goal'),
]
