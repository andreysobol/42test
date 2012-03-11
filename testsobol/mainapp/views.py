from django.views.generic import View, TemplateView
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from models import Bio, Request, RequestPriority
from forms import BioForm
from utils import DataRender


class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        super(Index, self).get_context_data(**kwargs)
        d = DataRender(Bio.objects.get(pk=1))
        return {'renders': d.render()}


class Edit(View):

    def render(self, request, form, temp):
        return render_to_response(temp,
            RequestContext(request, {'renders': form.render(), 'form': True}))

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(Edit, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = BioForm(model_to_dict(Bio.objects.get(pk=1)),
            {'img': Bio.objects.get(pk=1).img})
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


class Http(TemplateView):

    template_name = 'http.html'

    def get_context_data(self, **kwargs):

        def add(filter):

            req = Request.objects.exclude(url__in=exlude_list)

            if filter:
                req = req.filter(url=p.url)

            req = req.order_by('date')

            return [dict(model_to_dict(r).items() +
                ([('priority', p.priority)] if filter else [('priority', 0)]))
                for r in req]

        paginate_by = 10

        exlude_list = []
        result = []

        for p in RequestPriority.objects.order_by('-priority'):

            result += add(True)

            if len(result) > paginate_by:
                return {'custom_request': result[0:paginate_by]}
            else:
                exlude_list.append(p.url)

        result += add(False)

        return {'custom_request': (result if len(result) < paginate_by
            else result[0:paginate_by])}

    def get_queryset(self):
        return Request.objects.order_by('date')
