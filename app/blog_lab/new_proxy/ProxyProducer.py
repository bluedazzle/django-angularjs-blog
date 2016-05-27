# coding: utf-8

from __future__ import unicode_literals

import Queue
import threading


class BaseProducer(threading.Thread):
    def __init__(self, q, name='BasePro', pages=1):
        super(BaseProducer, self).__init__()
        self.q = q
        self.name = name
        self.pages = pages
        self.offset = 1
        self.url = ''
        self.type = 0

    def run(self):
        while True:
            resource = {}
            resource['url'] = '{0}{1}'.format(self.url, self.offset)
            resource['type'] = self.type
            try:
                self.q.put(resource, block=True, timeout=3)
            except Queue.Full:
                pass
            else:
                print '{0} now in queue'.format(self.offset)
                if self.offset < self.pages:
                    self.offset += 1
                else:
                    break
        print '{0} finish produce works'.format(self.name)


class XiCiProducer(BaseProducer):
    def __init__(self, q, name='XiCiPro', pages=713):
        super(XiCiProducer, self).__init__(q, name, pages)
        self.type = 1
        self.url = 'http://www.xicidaili.com/nn/'


class KuaiProducer(BaseProducer):
    def __init__(self, q, name='KuaiPro', pages=966):
        super(KuaiProducer, self).__init__(q, name, pages)
        self.type = 2
        self.url = 'http://www.kuaidaili.com/free/inha/'


class LiuLiuProducer(BaseProducer):
    def __init__(self, q, name='LiuLiuPro', pages=1):
        super(LiuLiuProducer, self).__init__(q, name, pages)
        self.type = 3
        self.url = 'http://www.66ip.cn/nmtq.php?getnum=10000&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip'

    def run(self):
        while True:
            resource = {}
            resource['url'] = self.url
            resource['type'] = self.type
            try:
                self.q.put(resource, block=True, timeout=3)
            except Queue.Full:
                pass
            else:
                break
        print '{0} finish produce works'.format(self.name)





