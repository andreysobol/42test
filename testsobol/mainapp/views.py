from django.views.generic import TemplateView, ListView
from django.forms.models import model_to_dict

from models import Bio, Request

class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return model_to_dict(Bio.objects.get(pk = 1))

class Http(ListView):

    context_object_name = 'request'
    template_name = 'http.html'
    paginate_by = 10

    def get_queryset(self):
        return Request.objects.order_by('-date')
