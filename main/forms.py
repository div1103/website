from .models import Task
from django.forms import ModelForm, widgets, TextInput, DateTimeInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "deadline", "location"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "task": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                   "deadline": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Срок выполнения'}),
                   "location": TextInput(attrs={'class': 'form-control', 'placeholder': 'Место выполнения'}),
                   }
