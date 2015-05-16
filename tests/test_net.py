import json

from django.test import TestCase

from app.NetProcess import *


class TestNetProcess(TestCase):
    def setUp(self):
        self.net = NetProcess()

    def test_create(self):
        net = NetProcess()
        net.Cookies = {'abc': 'cde'}
        net.Headers = {'header': True}
        net.Proxy = '192.168.1.1'
        self.assertEqual(net.Cookies, {'abc': 'cde'})
        self.assertEqual(net.Headers, {'header': True})
        self.assertEqual(net.Proxy, '192.168.1.1')

    def test_net_get(self):
        res = self.net.GetResFromRequest('GET', 'http://www.rapospectre.com')
        self.assertIsInstance(res, str)

    def test_net_post(self):
        postdict = {'private_token': 'rapospectre'}
        res = self.net.GetResFromRequest('POST', 'http://www.rapospectre.com/lab/get_proxy/', postDic=postdict)
        self.assertIsInstance(res, str)
        res_json = json.loads(res)
        self.assertEqual(res_json['status'], 1)

    def test_coroutine_net_req(self):
        postdict = {'private_token': 'rapospectre'}
        self.net.coroutine_request('POST', 'http://www.rapospectre.com/lab/get_proxy/', postDic=postdict)
        self.net.coroutine_request('POST', 'http://www.rapospectre.com/lab/get_proxy/', postDic=postdict)
        resp_list = self.net.coroutine_response()
        res_json = json.loads(resp_list[0].content)
        self.assertEqual(res_json['status'], 1)
        res_json = json.loads(resp_list[1].content)
        self.assertEqual(res_json['status'], 1)
