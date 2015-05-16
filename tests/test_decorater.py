import json

from django.test import TestCase
from mock import Mock
from django.test.client import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

from app.decorater import login_api, login_require, api_times, back_log
from app.blog_log.models import AccIP, ReqRecord, BackLog


class TestLoginRequire(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/blog/')
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()

    def test_login_req_no_user(self):
        func = Mock()
        decorat_func = login_require(func)
        resp = decorat_func(self.request)
        assert not func.called

    def test_login_req_user(self):
        func = Mock(return_value='success')
        decorat_func = login_require(func)
        self.request.session['user'] = 'rapo'
        resp = decorat_func(self.request)
        self.assertEqual(resp, 'success')

class TestLoginApi(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/blog_admin/know_opt')
        middleware = SessionMiddleware()
        middleware.process_request(self.request)
        self.request.session.save()

    def test_login_api_no_user(self):
        func = Mock()
        decorat_func = login_api(func)
        resp = decorat_func(self.request)
        jsonres = json.loads(resp.content)
        self.assertEqual(jsonres['status'], 9)
        assert not func.called

    def test_login_api_user(self):
        func = Mock(return_value='success')
        decorat_func = login_api(func)
        self.request.session['user'] = 'rapo'
        resp = decorat_func(self.request)
        self.assertEqual(resp, 'success')


class TestApiTimes(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/blog_admin/know_opt')

    def test_api_times(self):
        mock = Mock(return_value='success')
        func = api_times(mock)
        resp = func(self.request)
        self.assertEqual(resp, 'success')
        ip = AccIP.objects.get(ip=self.request.META['REMOTE_ADDR'])
        rr = ReqRecord.objects.get(ip=ip)
        self.assertEqual(rr.uri, '/blog_admin/know_opt')


class TestBackLog(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/blog_admin/know_opt')

    def test_back_log(self):
        mock = Mock(return_value='success')
        func_p = back_log(1)
        func = func_p(mock)
        resp = func(self.request)
        self.assertEqual(resp, 'success')
        back = BackLog.objects.get(content='success')
        self.assertEqual(back.content, 'success')