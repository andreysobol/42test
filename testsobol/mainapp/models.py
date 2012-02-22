from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birth = models.DateField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=250)
    other = models.TextField()
    bio = models.TextField()

class Request(models.Model):
    date = models.DateTimeField()
    url = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)
