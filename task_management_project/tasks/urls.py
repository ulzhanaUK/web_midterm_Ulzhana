from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('update/<int:id>/', views.task_update, name='task-update'),
    path('delete/<int:id>/', views.task_delete, name='task-delete'),
]
