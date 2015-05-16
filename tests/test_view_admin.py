from django.test import TestCase
from django.core.urlresolvers import reverse


class TestSimplePage(TestCase):
    def test_index(self):
        resp = self.client.get(reverse('admin_index'))
        self.assertEqual(resp.status_code, 200)

    def test_code(self):
        resp = self.client.get(reverse('admin_blog'))
        self.assertEqual(resp.status_code, 200)

    def test_blog(self):
        resp = self.client.get(reverse('admin_know'))
        self.assertEqual(resp.status_code, 200)

    def test_lab(self):
        resp = self.client.get(reverse('admin_new_know'))
        self.assertEqual(resp.status_code, 200)

    def test_about(self):
        resp = self.client.get(reverse('admin_modify_know', kwargs={'kid': 1}))
        self.assertEqual(resp.status_code, 200)

    def test_know(self):
        resp = self.client.get(reverse('admin_modify_blog', kwargs={'bid': 1}))
        self.assertEqual(resp.status_code, 200)

    def test_classify(self):
        resp = self.client.get(reverse('admin_new_blog'))
        self.assertEqual(resp.status_code, 200)
