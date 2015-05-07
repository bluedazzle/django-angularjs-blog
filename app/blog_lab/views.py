from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app.blog_lab.models import ProxyUser, Proxy
from app.blog_log.models import ReqRecord
from django.utils import timezone
from app.utils import datetime_to_string, encodejson
# Create your views here.

def proxy(req):
    return render_to_response("proxy.html")


def monitor(req):
    return render_to_response("monitor.html")


def get_proxy_info(req):
    body={}
    total_use = ProxyUser.objects.all().count()
    day_req = ReqRecord.objects.filter(uri='/lab/get_proxy').count()
    proxy_count = Proxy.objects.all().count()
    now_time = timezone.now()
    body['total_user'] = total_use
    body['req_times'] = day_req
    body['proxy_num'] = proxy_count
    body['update_time'] = datetime_to_string(now_time)
    return HttpResponse(encodejson(1, body), content_type="application/json")
