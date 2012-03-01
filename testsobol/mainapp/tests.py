"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import os
from datetime import datetime, timedelta
from subprocess import Popen, PIPE

from django.test import TestCase
from django.forms.models import model_to_dict

from models import Bio, Request, Log


class IndexViewTest(TestCase):

    def test(self):
        fixtures = ['initial_data.json']
        
        page = self.client.get('')

        self.assertEqual(page.status_code, 200)
        
        for key,value in model_to_dict(Bio.objects.get(pk = 1)).items():
            if key!='id':
                self.assertTrue(page.content.find(unicode(value)) != -1)


class RequestTest(TestCase):

    def test(self):
        page = self.client.get('')
        self.assertTrue(bool(Request.objects.filter(date__gte = (datetime.now() - timedelta(minutes=1)))))


class RequestViewTest(TestCase):

    def test(self):
        page = self.client.get('/http/')
        self.assertEqual(page.status_code, 200)
        self.assertTrue(bool(page.context['custom_request']))

class SettingsContextTest(TestCase):
    
    def test(self):
        page = self.client.get('')
        self.assertEqual(page.status_code, 200)
        self.assertTrue(page.context['settings'])


class Edit(TestCase):
    
    def test(self):
        fixtures = ['initial_data.json']

        page = self.client.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(page.status_code, 302)
        
        page = self.client.post('/edit/', {"bio": "Noooooooooooooo", "surname": "Sobol", "name": "Andrey", "other": "pigeon post - white pigeon only", "birth": "1990-09-18", "skype": "andreysobol", "jabber": "pisecs@gmail.com", "email": "asobol@mail.ua"})
        self.assertEqual(page.status_code, 200)
        self.assertTrue(page.content == 'Okay')
        self.assertTrue(Bio.objects.get(pk = 1).bio == "Noooooooooooooo")
        
        page = self.client.post('/edit/', {"bio": "Noooooooooooooo", "surname": "Sobol", "name": "Andrey", "other": "pigeon post - white pigeon only"})
        self.assertEqual(page.status_code, 200)
        self.assertTrue(page.content.find("error") != -1)


class AjaxEdit(TestCase):

    def test(self):
        fixtures = ['initial_data.json']
        
        page = self.client.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(page.status_code, 302)

        page = self.client.post('/edit/')
        self.assertTrue(page.content.find('<body>') == -1)
        
        page = self.client.get('/edit/')
        self.assertTrue(page.content.find('<body>') != -1)
        self.assertTrue(page.content.find('<script') != -1)

        page = self.client.get('/')
        self.assertTrue(page.content.find('<script') == -1)


class EditReverse(TestCase):

    def test(self):
        fixtures = ['initial_data.json']
        
        page = self.client.get('/')
        self.assertTrue(page.content.find('>Name:') < page.content.find('Last name:'))
        self.assertTrue(page.content.find('Bio:') > page.content.find('Other'))

        page = self.client.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})

        page = self.client.get('/edit/')
        self.assertTrue(page.content.find('>Name:') > page.content.find('Last name:'))
        self.assertTrue(page.content.find('Bio:') < page.content.find('Other'))


class Tag(TestCase):

    def test(self):
        fixtures = ['initial_data.json']

        page = self.client.post('/accounts/login/', {'username': 'admin', 'password': 'admin'})

        page = self.client.get('/')
        self.assertTrue(page.content.find('<a href="/admin/auth/user/1/"') != -1 )


class Command(TestCase):

    def test(self):
        p = Popen("python manage.py printmodels", stdout=PIPE, stderr=PIPE, shell=True).stdout.read()
        self.assertTrue(p.find('Bio')!=-1)
        Popen("bash save.bash", stdout=PIPE, stderr=PIPE, shell=True)
        l = os.listdir(".")
        for d in l:
            if d.find('.dat')!=-1:
                f = open(d,'r')
                self.assertTrue((f.read()).find('error') != -1)
                f.close()
                Popen("rm " + d, stdout=PIPE, stderr=PIPE, shell=True)


class Signal(TestCase):
    
    def test(self):
        b = Bio(bio="Noooooooooooooo", surname="Sobol", name="Andrey", other="pigeon post - white pigeon only", birth="1990-09-18", skype="andreysobol", jabber="pisecs@gmail.com", email="asobol@mail.ua", img="img/1.jpg")
        b.save()
        self.assertEqual(Log.objects.order_by('-id')[0].model,'Bio')
        self.assertEqual(Log.objects.order_by('-id')[0].signal,'create')
       
        b.bio="sfsf"
        b.save()
        self.assertEqual(Log.objects.order_by('-id')[0].model,'Bio')
        self.assertEqual(Log.objects.order_by('-id')[0].signal,'update')

        b.delete()
        self.assertEqual(Log.objects.order_by('-id')[0].model,'Bio')
        self.assertEqual(Log.objects.order_by('-id')[0].signal,'delete')

class RequestPriority(TestCase):

    def test(self):
        fixtures = ['initial_data.json']
        page = self.client.get('/http/')
        self.assertEqual(page.status_code, 200)
        b = False;
        for r in page.context['custom_request']:
            if r['url']=='/http/' and r['priority']==2:
                b = True
        self.assertTrue(b)
