"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Bio


class IndexViewTest(TestCase):
    def test(self):
        bio = Bio.objects.get(pk=1)
        page = self.client.get('')

        self.assertEqual(page.status_code, 200)

        lines = ('name', 'surname', 'birth', 'email',
                 'jabber', 'skype', 'bio', 'other',)
        for line in lines:
            self.assertEqual(page.context[line], getattr(bio, line))
