# -*- coding: utf-8 -*-
from app.blog_lab.models import Proxy
from app.blog_lab.proxy.Proxy import *

def get_proxy(args = None):
    a = NetProcess()
    a.Host = 'www.hao123.com'
    errmsg = ''
    myproxy = SProxy()
    ip_list = myproxy.renew_proxy()
    newitems = 0
    for item in ip_list:
        try:
            ishave = Proxy.objects.filter(ip = str(item))
            if ishave.count() > 0:
                continue
            a.Proxy = item
            res = a.GetResFromRequest('GET', "http://www.hao123.com/", 'utf-8', use_proxy=True)
            if isinstance(res, str):
                newitems += 1
                newproxy = Proxy()
                newproxy.ip = item
                newproxy.online = True
                newproxy.save()
        except Exception, e:
            except_handle(e)
            errmsg = str(e)
            continue
    content = '新增代理IP成功，新增数量' + str(newitems) + '条'
    print content


def check_proxy(args = None):
    a = NetProcess()
    useless = 0
    oters = Proxy.objects.all()
    for item in oters:
        a.Proxy = item.ip
        res = a.GetResFromRequest('GET', "http://www.hao123.com", 'utf-8', use_proxy=True)
        if not isinstance(res, str):
            item.delete()
            useless += 1
        else:
            # print res
            print item.ip + ' connect success'
    content = '代理检验完成，删除无效代理' + str(useless) + '个'
    print content