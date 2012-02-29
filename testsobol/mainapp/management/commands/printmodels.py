from django.core.management.base import NoArgsCommand
from django.db import models
import sys

class Command(NoArgsCommand):

    def handle(self, *args, **options):
        p = unicode([(cls.__name__,cls.objects.count()) for cls in models.get_models()])
        print p
        print >> sys.stderr, 'error: ' + p,
