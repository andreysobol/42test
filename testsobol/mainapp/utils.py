structs = (
    ('name', 'surname', 'birth', 'img'),
    ('email', 'jabber', 'skype', 'other', 'bio'),
)

multiline = ('bio', 'other', 'img')


class Render(object):

    def get_struct(self, get, reverse):
        if reverse:
            local_structs = [struct[::-1] for struct in structs]
        else:
            local_structs = structs
        return [[dict(get(item).items() + [('multiline', (item in multiline))])
            for item in struct]
            for struct in local_structs]


class DataRender(Render):

    def __init__(self, model):
        self.model = model

    def render(self):
        field_types = dict([(field.name, field.verbose_name) \
            for field in self.model._meta.fields])

        get = lambda item: {'value':\
            unicode(getattr(self.model, item)) if item != 'img'\
            else '<img src="%s" />' % getattr(self.model, item).url,
            'label': field_types[item]}

        return self.get_struct(get, False)
