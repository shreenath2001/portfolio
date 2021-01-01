from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 500)
    email = models.EmailField(max_length = 254)
    message = models.CharField(max_length = 2000)

    def __str__(self):
        return self.name

class Intro(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.CharField(max_length=300)
    twitter_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    image = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
