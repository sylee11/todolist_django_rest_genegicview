from django.urls import path, include
from .views import TaskView, TaskUpdate, TaskAdd
from .models import Tasks
from rest_framework.generics import CreateAPIView

urlpatterns = [
    path('/get_task', TaskView.as_view(), name = 'get_task'),
    path('/done_task/<int:id>', TaskUpdate.as_view(), name = 'task_update'),
    path('/add_task', TaskAdd.as_view(), name = 'task_add'),
]