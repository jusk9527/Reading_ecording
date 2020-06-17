# coding: utf-8
from __future__ import unicode_literals
from wsgiref import simple_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # print(start_response)
    return 'HTTP/1.1 200 OK\r\n\r\n<html><body>hello</body></html>'