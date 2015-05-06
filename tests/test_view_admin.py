from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from app.myblog.models import Article, Classification, Tag, Knowledge
from django.utils.importlib import import_module
import json

class TestSimplePage(TestCase):
    def test_index(self):
        resp = self.client.get(reverse('admin_index'))
        self.assertEqual(resp.status_code, 200)

def test_index(self):
        resp = self.client.get(reverse('admin_index'))
        self.assertEqual(resp.status_code, 200)

def test_blog(self):
        resp = self.client.get(reverse('admin_blog'))
        self.assertEqual(resp.status_code, 200)

def test_know(self):
        resp = self.client.get(reverse('admin_know'))
        self.assertEqual(resp.status_code, 200)

def test_new_know(self):
        resp = self.client.get(reverse('admin_new_know'))
        self.assertEqual(resp.status_code, 200)

def test_new_blog(self):
        resp = self.client.get(reverse('admin_new_blog'))
        self.assertEqual(resp.status_code, 200)

def test_modify_know(self):
        resp = self.client.get(reverse('admin_modify_know'))
        self.assertEqual(resp.status_code, 200)

def test_modify_blog(self):
        resp = self.client.get(reverse('admin_modify_blog'))
        self.assertEqual(resp.status_code, 500)