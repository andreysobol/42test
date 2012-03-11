from datetime import datetime

from models import Request


class RequestMiddleware(object):

    def process_request(self, request):
        r = Request()
        r.date = datetime.now()
        r.url = request.get_full_path()
        r.ip = request.get_host()
        r.save()
