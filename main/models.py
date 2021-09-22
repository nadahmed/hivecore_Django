from django.db import models
from django.db.models.base import Model

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    def __str__(self):
        return self.name

class Subtitle(models.Model):
    subtitle = models.TextField(max_length=1000)

class About(models.Model):
    caption = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'imag/%y', null=True, blank=True)
    def __str__(self):
        return self.caption

class Team(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'imag/%y', null=True, blank=True)
    facebook = models.TextField(max_length=50, null=True, blank=True)
    twitter = models.TextField(max_length=50, null=True, blank=True)
    social3 = models.TextField(max_length=50, null=True, blank=True)
    social4 = models.TextField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Team2(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'imag/%y', null=True, blank=True)
    facebook = models.TextField(max_length=50, null=True, blank=True)
    twitter = models.TextField(max_length=50, null=True, blank=True)
    social3 = models.TextField(max_length=50, null=True, blank=True)
    social4 = models.TextField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

class Clint_review(models.Model):
    clint_pic = models.ImageField(upload_to = 'imag/%y', null=True, blank=True)
    comment = models.TextField(max_length=1000)
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name

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

class Feature(models.Model):
    caption = models.CharField(max_length=50)
    details = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'imag/%y')
    def __str__(self):
        return self.caption