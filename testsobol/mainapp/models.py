from django.db import models

from utils import Render

class Bio(models.Model, Render):
    name = models.CharField(max_length=250, verbose_name='Name')
    surname = models.CharField(max_length=250, verbose_name='Last name')
    birth = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(verbose_name='Email')
    jabber = models.EmailField(verbose_name='Jabber')
    skype = models.CharField(max_length=250, verbose_name='Skype')
    other = models.TextField(verbose_name='Other contacts')
    bio = models.TextField(verbose_name='Bio')
    img = models.ImageField(verbose_name='Photo', upload_to='img/')

    def render(self):
        field_types = dict([(field.name, field.verbose_name) for field in self._meta.fields])

        get = lambda item: {'value':unicode(getattr(self,item)) if item!='img' else '<img src="%s" />' % getattr(self,item).url,'label':field_types[item]}

        return self.get_struct(get)


class Request(models.Model):
    date = models.DateTimeField()
    url = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)
