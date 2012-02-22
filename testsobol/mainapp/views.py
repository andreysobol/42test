from django.views.generic import TemplateView
from django.forms.models import model_to_dict

from models import Bio

class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return model_to_dict(Bio.objects.get(pk = 1))
