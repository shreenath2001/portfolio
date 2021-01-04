from django.shortcuts import redirect, render
from .models import Intro
from .models import Contact
from django.contrib import messages

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

def submit(request):
    return render(request, 'jobs/submit.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name = name, subject = subject, email = email, message = message)
        contact.save()
        messages.success(request, 'Form submission successful')
        return redirect('submit')
    return render(request, 'jobs/contact.html')
