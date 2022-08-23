from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput, DateInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "deadline", "location"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   "deadline": DateInput(attrs={'class': 'form-control', 'placeholder': 'Срок выполнения'}),
                   "location": TextInput(attrs={'class': 'form-control', 'placeholder': 'Место выполнения'}),
                   }
