from django.urls import path
from . import views

urlpatterns = [
    path('', views.GoalsBoardView.as_view(), name='goals_board'),
    path('create_goal/', views.CreateGoalView.as_view(), name='create_goal'),
    path('delete_goal/<slug:slug>/', views.delete_goal, name='delete_goal'),
    path('edit_goal/<slug:slug>/', views.EditGoalView.as_view(), name='edit_goal'),
    path('add_task/<slug:slug>/', views.add_task, name='add_task'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('edit_task/<slug:slug>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<slug:slug>/', views.delete_task, name='delete_task'),
    path('schedule_task/<slug:slug>/', views.schedule_task, name='schedule_task'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
]
