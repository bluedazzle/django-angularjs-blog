# -*- coding: utf-8 -*-
import datetime
import ujson

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import timezone
from dss.Serializer import serializer

from app.blog_lab.models import ProxyUser, Proxy
from app.blog_log.models import ReqRecord, BackLog
from app.utils import datetime_to_string, encodejson


# Create your views here.

def proxy(req):
    return render_to_response("proxy.html")


def monitor(req):
    return render_to_response("monitor.html")


def get_lab_info(req):
    body={}
    now = timezone.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    total_use = ProxyUser.objects.all().count()
    day_req = ReqRecord.objects.filter(uri='/lab/get_proxy/', create_time__gt=start).count()
    api_control = ReqRecord.objects.filter(create_time__gt=start).count()
    proxy_count = Proxy.objects.all().count()
    back_log = BackLog.objects.all()
    if back_log.exists():
        back_log = back_log.order_by('-create_time')
        new_time = datetime_to_string(back_log[0].create_time)
    else:
        new_time = '未更新'
    body['api_control'] = api_control
    body['api_status'] = True
    body['total_user'] = total_use
    body['req_times'] = day_req
    body['proxy_num'] = proxy_count
    body['update_time'] = new_time
    return HttpResponse(encodejson(1, body), content_type="application/json")

def hy_sign(req):
    hylog_list = BackLog.objects.filter(log_type=30)
    hylogs = serializer(hylog_list, datetime_format='string')
    for itm in hylogs:
        if itm['status'] is False:
            jsonr = itm['fail_message']
            jsonr = eval(jsonr)
            itm['fail_message'] = jsonr['msg']
    return render_to_response('hy.html', {'hylog_list': hylogs})
