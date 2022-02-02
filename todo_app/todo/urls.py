from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('new/', views.TodoNew, name='new'),
    path('created/', views.TodoCreated),
    path('list/', views.TodoListView.as_view()),
    path('single/', views.TodoSingleView.as_view(), name='single'),
    path('delete_get/<int:todo_id>/', views.TodoDeleteView, name='delete_get'),
    path('update_checks/', views.TodoUpdateChecks),
]