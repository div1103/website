from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница', 'tasks': tasks})

def contact(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def create(request):
    return render(request, 'create.html')
# Create your views here.
