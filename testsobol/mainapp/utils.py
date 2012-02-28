structs = ( 
    ('name','surname','birth','img'), 
    ('email','jabber','skype','other', 'bio'),
)

multiline = ('bio','other', 'img')

class Render(object):
    
    def get_struct(self, get, reverse):
        if reverse:
            local_structs = [struct[::-1] for struct in structs]
        else:
            local_structs = structs
        return [[dict(get(item).items() + [('multiline',(item in multiline))]) for item in struct] for struct in local_structs]
