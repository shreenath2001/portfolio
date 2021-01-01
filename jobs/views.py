from django.shortcuts import render
from .models import Intro

# Create your views here.

def home(request):
    intro = Intro.objects.get(first_name = "Shreenath")
    data = {
        'intro':intro,
    }
    return render(request, 'jobs/home.html', data)
