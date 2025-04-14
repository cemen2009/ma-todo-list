from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


# tasks
class TasksListView(ListView):
    model = Task
    template_name = "todo/home.html"
    context_object_name = "tasks"
    queryset = Task.objects.all().order_by("is_done", "-created_at")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Task"
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Task'
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")
    template_name = "todo/task_confirm_delete.html"


class TaskToggleView(RedirectView):
    pattern_name = "todo:home"

    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return reverse("todo:home")


# tags
class TagListView(ListView):
    model = Tag
    template_name = "todo/tags.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Tag"
        return context


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"
