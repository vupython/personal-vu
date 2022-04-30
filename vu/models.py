from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'vu/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
