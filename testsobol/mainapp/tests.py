"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase

from models import Bio, Request


class IndexViewTest(TestCase):

    def test(self):
        fixtures = ['initial_data.json']
        bio = Bio.objects.get(pk = 1)
        page = self.client.get('')

        self.assertEqual(page.status_code, 200)

        lines = ('name','surname','birth','email','jabber','skype','bio','other',)
        for line in lines:
            self.assertEqual(page.context[line],getattr(bio,line))


class RequestTest(TestCase):

    def test(self):
        page = self.client.get('')
        self.assertTrue(bool(Request.objects.filter(date__lte = (datetime.now() - timedelta(minutes=1)))))


class RequestViewTest(TestCase):

    def test(self):
        page = self.client.get('/http/')
        self.assertEqual(page.status_code, 200)
        self.assertTrue(bool(page.context['request']))
