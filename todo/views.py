from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task


class TasksListView(ListView):
    model = Task
    template_name = "todo/home.html"
