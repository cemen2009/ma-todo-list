from django.urls import path

from todo.views import TasksListView

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="home"),
]
