# coding: utf-8

from __future__ import unicode_literals

from app.blog_lab.models import Proxy

import Queue
import threading
import requests


class CheckConsumer(threading.Thread):
    def __init__(self, cq, proxy='', name='ChkCon'):
        super(CheckConsumer, self).__init__()
        self.cq = cq
        self.name = name
        self.check_url1 = 'http://www.so.com'
        self.check_url2 = 'http://www.bing.com'
        self.check_url3 = 'http://www.zhihu.com'
        self.proxies = {
            'http': proxy,
            'https': proxy
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
            'Content-Type': 'text/html'
        }

    @property
    def proxy(self):
        return self.proxies['http']

    @proxy.setter
    def proxy(self, proxy):
        self.proxies['https'] = proxy
        self.proxies['http'] = proxy

    def run(self):
        while True:
            try:
                addr = self.cq.get(block=True, timeout=3)
                self.proxy = addr
                if self.check_proxy():
                    print 'ip {0} is available'.format(addr)
                    self.save_addr(addr)
                self.cq.task_done()
            except Queue.Empty:
                break
            except Exception, e:
                print e
        print '{0} finish Check work'.format(self.name)

    def _request(self, url):
        try:
            res = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=4)
        except Exception, e:
            return False
        else:
            if res.status_code == 200:
                return True
            else:
                return False

    def check_proxy(self):
        check_one = self._request(self.check_url1)
        check_two = self._request(self.check_url2)
        check_three = self._request(self.check_url3)
        return check_one or check_two or check_three

    def save_addr(self, addr):


