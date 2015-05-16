import random
import copy

from django.http import HttpResponse

from app.utils import create_token, encodejson
from app.blog_lab.models import Proxy, ProxyUser
from app.utils import datetime_to_string
from app.decorater import api_times


@api_times
def create_permission(req):
    body={}
    ip = req.META['REMOTE_ADDR']
    token = create_token()
    new_user = ProxyUser(token=token, ip=ip)
    new_user.save()
    body['private_token'] = token
    return HttpResponse(encodejson(1, body), content_type="application/json")


@api_times
def get_ip(req):
    body={}
    token = req.POST.get('private_token', None)
    reset = req.POST.get('reset', False)
    if token is None:
        body['msg'] = 'missing required parameter: private_token'
        return HttpResponse(encodejson(7, body), content_type="application/json")
    p_user_list = ProxyUser.objects.filter(token=token)
    if not p_user_list.exists():
        body['msg'] = 'invalid private_token'
        return HttpResponse(encodejson(6, body), content_type="application/json")
    user = p_user_list[0]
    ip_list = Proxy.objects.all()
    ip_count = ip_list.count()
    req_list = []
    reqed = user.record.split(',')
    for i in range(0, 5):
        r_num = random.randint(1, ip_count)
        proxy = ip_list[(r_num - 1)]
        if str(proxy.id) in reqed:
            r_num = random.randint(1, ip_count)
            proxy = ip_list[(r_num - 1)]
        ip_body={}
        ip_body['ip'] = proxy.ip
        ip_body['id'] = proxy.id
        ip_body['create_time'] = datetime_to_string(proxy.create_time)
        ip_body['modify_time'] = datetime_to_string(proxy.modify_time)
        req_list.append(copy.copy(ip_body))
        if str(proxy.id) not in reqed:
            user.record = user.record + str(proxy.id) + ','
    user.save()
    body['proxy_list'] = req_list
    return HttpResponse(encodejson(1, body), content_type="application/json")