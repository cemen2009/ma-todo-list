from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "What to do?",
            "rows": 2
        }),
        help_text="Enter your task here",
    )

    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local"
        }),
        help_text="Leave empty if there is no specific deadline"
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {"tags": forms.CheckboxSelectMultiple}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
