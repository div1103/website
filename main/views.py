from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')
# Create your views here.
