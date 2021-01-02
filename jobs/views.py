from django.shortcuts import render
from .models import Intro

# Create your views here.

def home(request):
    intro = Intro.objects.get(first_name = "Shreenath")
    data = {
        'intro':intro,
    }
    return render(request, 'jobs/home.html', data)

def about(request):
    return render(request, 'jobs/about.html')

def work(request):
    return render(request, 'jobs/work.html')

def projects(request):
    return render(request, 'jobs/projects.html')

def contact(request):
    return render(request, 'jobs/contact.html')
