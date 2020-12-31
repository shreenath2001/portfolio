from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    contacts = Contact.objects.all()
    data = {
        'contacts':contacts,
    }
    return render(request, 'jobs/home.html', data)
