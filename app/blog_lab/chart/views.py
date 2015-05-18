# -*- coding: utf-8 -*-
import datetime
import copy

from django.utils import timezone
from django.http import HttpResponse

from app.blog_log.models import AccIP, ReqRecord
from app.decorater import api_times
from app.utils import encodejson


@api_times
def get_chart_message(req):
    body = {}
    now = timezone.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    record_list = ReqRecord.objects.filter(create_time__gt=start).values('uri').distinct()
    day_rec_list = []
    day_rec_count = []
    for itm in record_list:
        rec_count = ReqRecord.objects.filter(create_time__gt=start, uri=itm['uri']).count()
        day_rec_list.append(copy.copy(itm['uri']))
        day_rec_count.append(copy.copy(rec_count))
    body['req_rec'] = day_rec_list
    body['req_count'] = day_rec_count
    record_list = ReqRecord.objects.filter(create_time__gt=start).values('ip').distinct()
    day_ip_list = []
    day_ip_count = []
    for itm in record_list:
        ip_count = ReqRecord.objects.filter(create_time__gt=start, ip=itm['ip']).count()
        tip = AccIP.objects.get(id=itm['ip']).ip
        day_ip_list.append(copy.copy(tip))
        day_ip_count.append(copy.copy(ip_count))
    body['ip_rec'] = day_ip_list
    body['ip_count'] = day_ip_count
    return HttpResponse(encodejson(1, body), content_type="application/json")
