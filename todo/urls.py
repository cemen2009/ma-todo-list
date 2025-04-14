from django.urls import path

from todo.views import TasksListView, TagListView, TaskUpdateView, TaskCreateView, TaskDeleteView, TaskToggleView, \
    TagCreateView, TagUpdateView, TagDeleteView

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag-list"),

    path("task/add/", TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", TaskToggleView.as_view(), name="task-toggle"),

    path("tag/add/", TagCreateView.as_view(), name="tag-add"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
