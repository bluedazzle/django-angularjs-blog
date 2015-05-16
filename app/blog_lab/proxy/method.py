# -*- coding: utf-8 -*-
from app.blog_lab.models import Proxy
from app.blog_lab.proxy.Proxy import *
from app.decorater import back_log
from app.decorater import BACK_CHECK_PROXY, BACK_GET_PROXY

@back_log(BACK_GET_PROXY)
def get_proxy(args = None):
    a = NetProcess()
    a.Host = 'www.hao123.com'
    errmsg = ''
    in_queue = 0
    myproxy = SProxy()
    ip_list = myproxy.renew_proxy()
    newitems = 0
    for item in ip_list:
        try:
            ishave = Proxy.objects.filter(ip = str(item))
            if ishave.count() > 0:
                continue
            a.Proxy = item
            in_queue += 1
            a.coroutine_request('GET', "http://www.hao123.com/", 'utf-8', use_proxy=True)
        except Exception, e:
            continue
    print '%d proxy in queue' % in_queue
    print 'start requests...'
    resp_list = a.coroutine_response(status_only=True)
    for i, itm in enumerate(resp_list):
        ishave = Proxy.objects.filter(ip=str(ip_list[i])).exists()
        if itm and not ishave:
            new_proxy = Proxy(ip=ip_list[i])
            new_proxy.save()
            newitems += 1
    content = '新增代理IP成功，新增数量' + str(newitems) + '条'
    print content
    return content

@back_log(BACK_CHECK_PROXY)
def check_proxy(args = None):
    a = NetProcess()
    useless = 0
    oters = Proxy.objects.all()
    for item in oters:
        a.Proxy = item.ip
        a.coroutine_request('GET', "http://www.hao123.com", 'utf-8', use_proxy=True)
    print '%d proxy in queue' % oters.count()
    print 'start requests...'
    resp_list = a.coroutine_response(status_only=True)
    for i, itm in enumerate(resp_list):
        if not itm:
            oters[i].delete()
            useless += 1
        else:
            oters[i].save()
    content = '代理检验完成，删除无效代理' + str(useless) + '个'
    print content
    return content