from django.views.generic import View, TemplateView, ListView
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from models import Bio, Request
from forms import BioForm


class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        super(Index, self).get_context_data(**kwargs)
        return {'renders': Bio.objects.get(pk=1).render()}


class Edit(View):
    
    def render(self, request, form, temp):
        return render_to_response(temp,
            RequestContext(request, {'renders': form.render(), 'form': True}))

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(Edit, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = BioForm(model_to_dict(Bio.objects.get(pk=1)),
            {'img':Bio.objects.get(pk=1).img})
        return self.render(request, form, 'index.html')

    def post(self, request):
        if not request.FILES:
            form = BioForm(request.POST, {'img': Bio.objects.get(pk=1).img})
        else:
            form = BioForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.id = 1
            model.save()
            return HttpResponse("Okay")
        else:
            return self.render(request, form, 'content.html')


class Http(ListView):

    context_object_name = 'request'
    template_name = 'http.html'
    paginate_by = 10

    def get_queryset(self):
        return Request.objects.order_by('date')
