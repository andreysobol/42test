from django.db import models
from django.db.models.signals import post_save, post_delete


class Bio(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    surname = models.CharField(max_length=250, verbose_name='Last name')
    birth = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(verbose_name='Email')
    jabber = models.EmailField(verbose_name='Jabber')
    skype = models.CharField(max_length=250, verbose_name='Skype')
    other = models.TextField(verbose_name='Other contacts')
    bio = models.TextField(verbose_name='Bio')
    img = models.ImageField(verbose_name='Photo', upload_to='img/')


class Request(models.Model):
    date = models.DateTimeField()
    url = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)

class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=250)
    signal = models.CharField(max_length=250)

def save(sender, **kwargs):
    if sender != Log:
        if kwargs['created']:
            signal='create'
        else:
            signal='update'

        log = Log(model = sender.__name__, signal = signal)
        log.save()

def delete(sender, **kwargs):
    log = Log(model = sender.__name__, signal = 'delete')
    log.save()

post_save.connect(save)
post_delete.connect(delete)
