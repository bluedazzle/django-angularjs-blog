from django.http import HttpResponse
from django.shortcuts import render_to_response

from app.utils import *
from app.blog_log.models import AccIP, ReqRecord, BackLog


BACK_GET_PROXY = 1
BACK_CHECK_PROXY = 2

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



def api_times(func):
    def exect(*args, **kw):
        req = args[0]
        ip = req.META['REMOTE_ADDR']
        uri = req.META['PATH_INFO']
        api_t = AccIP.objects.get_or_create(ip=ip)[0]
        api_t.total += 1
        api_t.day_count += 1
        api_t.save()
        new_record = ReqRecord(uri=uri, ip=api_t)
        new_record.save()
        res = func(*args, **kw)
        return res
    return exect



def back_log(ltype):
    def back_type(func):
        def exect(*args, **kw):
            if ltype == 1:
                new_back = BackLog(log_type=1)
            if ltype == 2:
                new_back = BackLog(log_type=2)
            else:
                new_back = BackLog(log_type=2)
            res = func(*args, **kw)
            new_back.content = res
            new_back.save()
            return res
        return exect
    return back_type
