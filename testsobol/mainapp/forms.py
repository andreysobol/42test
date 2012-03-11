from django.forms import ModelForm, ClearableFileInput
from django.utils.html import escape
from django.utils.safestring import mark_safe

from models import Bio
from utils import Render


class ImgWidget(ClearableFileInput):

    def render(self, name, value, attrs=None):
        substitutions = {}
        template = u'%(input)s'
        substitutions['input'] = super(ClearableFileInput, self)\
            .render(name, value, attrs)
        if value and hasattr(value, "url"):
            template = u'%(initial)s<br />%(input)s'
            substitutions['initial'] = (u'<img src="%s"/>' %\
                (escape(value.url)))
        return mark_safe(template % substitutions)


class BioForm(ModelForm, Render):
    class Meta:
        model = Bio
        widgets = {
            'img': ImgWidget(),
        }

    def render(self):
        form_field = dict([(field.name,
            {'label':field.label,
            'value':field.as_widget(),
            'errors':field.errors}) for field in self])

        get = lambda item: form_field[item]

        return self.get_struct(get, True)
