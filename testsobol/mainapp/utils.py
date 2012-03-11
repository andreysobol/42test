structs = (
    ('name', 'surname', 'birth', 'img'),
    ('email', 'jabber', 'skype', 'other', 'bio'),
)

multiline = ('bio', 'other', 'img')


class Render(object):

    def get_struct(self, get):
        return [[dict(get(item).items() + [('multiline', (item in multiline))])
            for item in struct]
            for struct in structs]
