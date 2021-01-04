from django.shortcuts import redirect, render
from .models import Intro
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                subject,
                message,
                'bharadwajshreenath@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        contact.save()
        return redirect('submit')
    return render(request, 'jobs/contact.html')
