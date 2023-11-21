from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.GoalsBoardView.as_view(), name='goals_board'),
    path('create_goal/', views.CreateGoalView.as_view(), name='create_goal'),
    path('goal_detail/<slug:slug>/', views.GoalDetailView.as_view(), name='goal_detail'),
    path('delete_goal/<slug:slug>/', views.delete_goal, name='delete_goal'),
    path('edit_goal/<slug:slug>/', views.EditGoalView.as_view(), name='edit_goal'),
    path('progress_status/<slug:slug>/', views.select_progress_status, name='progress_status'),
    path('on_hold_status/<slug:slug>/', views.select_on_hold_status, name='on_hold_status'),
    path('done_status/<slug:slug>/', views.select_done_status, name='done_status'),
    path('add_task/<slug:slug>/', views.add_task, name='add_task'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('edit_task/<slug:slug>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<slug:slug>/', views.delete_task, name='delete_task'),
    path('schedule_task/<slug:slug>/', views.schedule_task, name='schedule_task'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('api/calendar_data/', views.calendar_data, name='calendar_data'),
    path('delete_scheduled_task/<slug:slug>/', views.delete_scheduled_task, name='delete_scheduled_task'),
    path('edit_scheduled_task/<slug:slug>/', views.edit_scheduled_task, name='edit_scheduled_task'),
    path('complete_scheduled_task/<slug:slug>/', views.complete_scheduled_task, name='complete_scheduled_task'),
]

handler404 = views.custom_404_view