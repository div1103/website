from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    form = TaskForm()
    return render(request, 'index.html', {'title': 'Главная страница', 'tasks': tasks, 'form': form})

def contact(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def create(request):
    form = TaskForm()
    context = {
        'form':form
    }
    return render(request, 'create.html', context)


# Create your views here.
