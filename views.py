import json
import os
import logging
from django.http import HttpResponse
from .utils import SetupGame


class PLAYGAME:

    def __init__(self, **kwargs):
        self.classname = "PLAYGAME"

    def post(self, request):
        request_body = json.loads(request.body)

        service = SetupGame(request_body.get("snake", None),
                            request_body.get("ladder", None),
                            request_body.get("dice", None),
                            request_body.get("board", None),
                            request_body.get("player", None))
        response = service.play()
        return HttpResponse(json.dumps(response))



