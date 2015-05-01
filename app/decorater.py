from django.http import HttpResponse
from app.utils import *
from django.shortcuts import render, render_to_response


def login_api(func):
    def exect(*args, **kw):
        body = {}
        req = args[0]
        user = req.session.get('user', None)
        if user is None or user == '':
            return HttpResponse(encodejson(9, body), content_type="application/json")
        res = func(*args, **kw)
        return res
    return exect


def login_require(func):
    def exect(*args, **kw):
        body = {}
        req = args[0]
        user = req.session.get('user', None)
        if user is None or user == '':
            return render_to_response("badmin.html")
        res = func(*args, **kw)
        return res
    return exect

