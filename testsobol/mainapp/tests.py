"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase
from django.forms.models import model_to_dict

from models import Bio, Request


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
        self.assertTrue(bool(page.context['request']))

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
