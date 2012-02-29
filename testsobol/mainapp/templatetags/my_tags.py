from django.template import Library, Node, Variable
from django.core.urlresolvers import reverse

register = Library()

class EditAdmin(Node):

    def __init__(self, edit):
        self.edit = Variable(edit)

    def render(self, context):
        e = self.edit.resolve(context)
        return u'<a href="%s">Edit</a>' % reverse('admin:%s_%s_change' % (e._meta.app_label, e._meta.module_name), args=(e.id,))


def ed(parser, token):
    return EditAdmin(token.split_contents()[1])

register.tag('ed', ed)
