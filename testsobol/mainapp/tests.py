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
        bio = Bio.objects.get(pk=1)
        page = self.client.get('')

        self.assertEqual(page.status_code, 200)

        lines = ('name', 'surname', 'birth', 'email',
                 'jabber', 'skype', 'bio', 'other',)
        for line in lines:
            self.assertEqual(page.context[line], getattr(bio, line))


class RequestTest(TestCase):

    def test(self):
        page = self.client.get('')

        self.assertEqual(page.status_code, 200)

        self.assertTrue(bool(Request.objects.filter(
            date__gte=(datetime.now() - timedelta(minutes=1)))))


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


class NameUrlTest(TestCase):

    def test(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTrue(page.content.find('a href="/http/"') != -1)


class ManyRequestTest(TestCase):

    def test(self):
        for t in range(11):
            page = self.client.get('/')
            self.assertEqual(page.status_code, 200)

        page = self.client.get('/http/')
        self.assertTrue(page.context['request'].count() == 10)
