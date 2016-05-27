# coding: utf-8

from __future__ import unicode_literals

import re
import requests

from bs4 import BeautifulSoup


class BaseSpider(object):
    def __init__(self, url):
        super(BaseSpider, self).__init__()
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
                        'Content-Type': 'text/html'}
        self.cookies = None
        self.content = None
        self.addr_list = list()

    def run(self):
        session = requests.session()
        res = session.get(self.url, headers=self.headers)
        self.content = res.text
        return self._extract_address()

    def _extract_address(self):
        pass


class XiCiSpider(BaseSpider):
    def __init__(self, url):
        super(XiCiSpider, self).__init__(url)

    def _extract_address(self):
        soup = BeautifulSoup(self.content)
        tr_res = soup.findAll('tr')
        for i in range(1, len(tr_res)):
            td_res = tr_res[i].findAll('td')
            ip = '{0}:{1}'.format(str(td_res[2].string), str(td_res[3].string))
            self.addr_list.append(ip)
        return self.addr_list


class KuaiSpider(BaseSpider):
    def __init__(self, url):
        super(KuaiSpider, self).__init__(url)

    def _extract_address(self):
        soup = BeautifulSoup(self.content)
        tr_res = soup.findAll('tr')
        for i in range(1, len(tr_res)):
            td_res = tr_res[i].findAll('td')
            ip = '{0}:{1}'.format(str(td_res[0].string), str(td_res[1].string))
            self.addr_list.append(ip)
        return self.addr_list


class LiuLiuSpider(BaseSpider):
    def __init__(self, url):
        super(LiuLiuSpider, self).__init__(url)

    def _extract_address(self):
        match_res = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', self.content)
        for itm in match_res:
            self.addr_list.append(itm)
        return self.addr_list


class SpiderFactory(object):
    def __init__(self):
        super(SpiderFactory, self).__init__()

    def create_spider(self, resource):
        spider_type = resource['type'] - 1
        spider_tuple = (XiCiSpider, KuaiSpider, LiuLiuSpider)
        return spider_tuple[spider_type](resource['url'])
