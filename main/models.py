from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()

class Subtitle(models.Model):
    subtitle = models.TextField(max_length=1000)

class About(models.Model):
    description = models.TextField(max_length=1000)

class About_image(models.Model):
    image = models.ImageField(upload_to = 'imag/%y')


class Mission(models.Model):
    moto = models.TextField(max_length=1000)

class Logo(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'imag/%y')
    def __str__(self):
        return self.caption

class Banner(models.Model):
    image = models.ImageField(upload_to = 'imag/%y')

class Nav_logo(models.Model):
    image = models.ImageField(upload_to = 'imag/%y')

class Footer(models.Model):
    image = models.ImageField(upload_to = 'imag/%y')