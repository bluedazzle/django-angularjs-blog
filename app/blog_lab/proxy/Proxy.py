# -*- coding: utf-8 -*-
import re
import copy

from bs4 import BeautifulSoup

from app.NetProcess import *


class SProxy(object):
    def __init__(self):
        self.HttpR = NetProcess()
        self.XICIURL = 'http://www.xici.net.co/nn/'
        self.KUAI = 'http://www.kuaidaili.com/free/inha/'
        self.CNPROXY = 'http://cn-proxy.com/'
        self.ip_list = []

    def open_file(self, filename):
        with open(filename, 'r') as f1:
            html = ''
            line = f1.readline()
            while line:
                html += line
                line = f1.readline()
        f1.close()
        return html

    def get_proxy_from_xici(self):
        flag = 0
        # self.HttpR.Host = 'www.xici.net.co'
        for j in range(1, 4):
            try:
                res = self.HttpR.GetResFromRequest('GET', self.XICIURL + str(j), 'utf-8')
                if res is None:
                    flag += 1
                    continue
                soup = BeautifulSoup(res)
                tr_res = soup.findAll('tr')
                # print len(tr_res)
                for i in range(1, len(tr_res)):
                    td_res = tr_res[i].findAll('td')
                    ip = str(td_res[2].string) + ':' + str(td_res[3].string)
                    self.ip_list.append(copy.copy(ip))
            except Exception, e:
                # print e
                continue
        if flag == 3:
            return False
        return True

    def get_proxy_from_kuai(self):
        flag = 0
        # self.HttpR.Host = 'www.kuaidaili.com'
        for j in range(1, 4):
            try:
                res = self.HttpR.GetResFromRequest('GET', self.KUAI + str(j) + '/', 'utf-8')
                if res is None:
                    flag += 1
                    continue
                soup = BeautifulSoup(res)
                tr_res = soup.findAll('tr')
                for i in range(1, len(tr_res)):
                    td_res = tr_res[i].findAll('td')
                    ip = str(td_res[0].string) + ':' + str(td_res[1].string)
                    self.ip_list.append(copy.copy(ip))
            except Exception, e:
                # print e
                continue
        if flag == 3:
            return False
        return True

    def get_proxy_from_cnproxy(self):
        # self.HttpR.Host = 'cn-proxy.com'
        html = self.HttpR.GetResFromRequest('GET', self.CNPROXY, 'utf-8')
        soup = BeautifulSoup(html)
        s = soup.findAll('tr')
        for i in range(2, len(s)):
            try:
                speed = s[i].findAll('td')[3]
                speedres = speed.find('strong', attrs={'class': 'bar'})
                reres = re.findall(r'width[: ]+(\d{1,3})[%]', speedres['style'])
                if int(reres[0]) > 59:
                    proxip = s[i].findAll('td')[0].string+':'+s[i].findAll('td')[1].string
                    self.ip_list.append(copy.copy(proxip))
            except Exception, e:
                # print e
                continue
        return True

    def renew_proxy(self):
        self.ip_list = []
        self.get_proxy_from_cnproxy()
        self.get_proxy_from_xici()
        self.get_proxy_from_kuai()
        return self.ip_list
