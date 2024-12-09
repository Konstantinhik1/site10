from itertools import count
from symtable import Class

from django.http import HttpResponse, HttpRequest


def set_useragent_on_request_middleware(get_response):

    print("initial call")

    def middleware(request: HttpResponse):
        print("before get_response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware

class CountRequestsMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        self.request_count = 0
        self.responses_count = 0
        self.exception_count = 0

    def __call__(self, request: HttpRequest):
        self.request_count += 1
        print("requests count", self.request_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response

    def process_exeption(self,request: HttpRequest, Exception):
        self.exception_count += 1
        print("got", self.exception_count, "exceptions so far")