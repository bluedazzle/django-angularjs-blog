import json

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.importlib import import_module

from app.myblog.models import Article, Classification, Tag, Knowledge


class TestSimplePage(TestCase):
    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_code(self):
        resp = self.client.get(reverse('code'))
        self.assertEqual(resp.status_code, 200)

    def test_blog(self):
        resp = self.client.get(reverse('blog'))
        self.assertEqual(resp.status_code, 200)

    def test_lab(self):
        resp = self.client.get(reverse('lab'))
        self.assertEqual(resp.status_code, 200)

    def test_about(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_know(self):
        resp = self.client.get(reverse('know'))
        self.assertEqual(resp.status_code, 200)

    def test_classify(self):
        resp = self.client.get(reverse('classify', kwargs={'bid': 1}))
        self.assertEqual(resp.status_code, 200)

    def test_tag(self):
        resp = self.client.get(reverse('tag', kwargs={'bid': 1}))
        self.assertEqual(resp.status_code, 200)


class TestSubmitComment(TestCase):
    def setUp(self):
        classify = Classification.objects.create(c_name='test')
        self.art = Article.objects.create(caption='article',
                                          sub_caption='sub_article',
                                          classification=classify,
                                          content='article test',
                                          publish=True)
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    def test_submit(self):
        self.session['verify'] = '1234'
        self.session.save()
        resp = self.client.post(reverse('submit_comment', kwargs={'bid': self.art.id}), {'verify': '1234',
                                                                                         'content': 'test',
                                                                                         'nick': 'test'})
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_verify(self):
        resp = self.client.post(reverse('submit_comment', kwargs={'bid': self.art.id}), {'verify': '1234',
                                                                                         'content': 'test',
                                                                                         'nick': 'test'})
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 12)

    def test_no_exist(self):
        self.session['verify'] = '1234'
        self.session.save()
        resp = self.client.post(reverse('submit_comment', kwargs={'bid': 100}), {'verify': '1234',
                                                                                 'content': 'test',
                                                                                 'nick': 'test'})
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 7)


class TestRefreshVerify(TestCase):
    def test_create(self):
        resp = self.client.get(reverse('verify_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)


class TestGetIndex(TestCase):
    def test_get(self):
        classify = Classification.objects.create(c_name='test')
        Article.objects.create(caption='article',
                               sub_caption='sub_article',
                               classification=classify,
                               content='article test',
                               publish=True)
        resp = self.client.get(reverse('index_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_get_blank(self):
        resp = self.client.get(reverse('index_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 7)


class TestGetArticleByClassify(TestCase):
    def setUp(self):
        self.classify = Classification.objects.create(c_name='test')
        Article.objects.create(caption='article',
                               sub_caption='sub_article',
                               classification=self.classify,
                               content='article test',
                               publish=True)

    def test_get_blog_by_classify(self):
        resp = self.client.get(reverse('classify_json', kwargs={'cid': self.classify.id}))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_pagination(self):
        resp = self.client.get(reverse('classify_json', kwargs={'cid': self.classify.id}), {'page': 2})
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['total'], 1)
        self.assertEqual(pagination['total_page'], 1)
        self.assertEqual(pagination['pre'], 1)
        self.assertEqual(pagination['next'], 0)
        self.assertEqual(pagination['page'], 2)

        resp = self.client.get(reverse('classify_json', kwargs={'cid': self.classify.id}), {'page': 'test'})
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['page'], 1)


class TestGetArticleByTag(TestCase):
    def setUp(self):
        self.classify = Classification.objects.create(c_name='test')
        self.tag = Tag.objects.create(tag_name='test')
        art = Article.objects.create(caption='article',
                                     sub_caption='sub_article',
                                     classification=self.classify,
                                     content='article test',
                                     publish=True)
        art.tags.add(self.tag)
        art.save()

    def test_get_blog_by_tag(self):
        resp = self.client.get(reverse('tag_json', kwargs={'tid': self.classify.id}))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def tes_pagination(self):
        resp = self.client.get(reverse('tag_json', kwargs={'cid': self.tag.id}), {'page': 2})
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['total'], 1)
        self.assertEqual(pagination['total_page'], 1)
        self.assertEqual(pagination['pre'], 1)
        self.assertEqual(pagination['next'], 0)
        self.assertEqual(pagination['page'], 2)

        resp = self.client.get(reverse('tag_json', kwargs={'cid': self.tag.id}), {'page': 'test'})
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['page'], 1)


class TestSearchKnow(TestCase):
    def setUp(self):
        Knowledge.objects.create(question='test',
                                 answer='answer',
                                 publish=True)

    def test_search(self):
        resp = self.client.get(reverse('know_json_text', kwargs={'text': 'te'}))
        self.assertEqual(resp.status_code, 200)
        json_res = json.loads(resp.content)
        know_list = json_res['body']['know_list']
        know = know_list[0]
        self.assertEqual(know['question'], 'test')

    def test_get(self):
        resp = self.client.get(reverse('know_json_text', kwargs={'text': None}))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_pagination(self):
        resp = self.client.get((reverse('know_json_text', kwargs={'text': None})), {'page': 2})
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['total'], 1)
        self.assertEqual(pagination['total_page'], 1)
        self.assertEqual(pagination['pre'], 1)
        self.assertEqual(pagination['next'], 0)
        self.assertEqual(pagination['page'], 2)


class TestDetail(TestCase):
    def setUp(self):
        self.classify = Classification.objects.create(c_name='test')
        self.tag = Tag.objects.create(tag_name='test')
        self.art = Article.objects.create(caption='article',
                                          sub_caption='sub_article',
                                          classification=self.classify,
                                          content='article test',
                                          publish=True)
        self.art.tags.add(self.tag)
        self.art.save()

    def test_deatil(self):
        resp = self.client.get(reverse('detail_json_id', kwargs={'bid': self.art.id}))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_pagnination(self):
        resp = self.client.get(reverse('detail_json_id', kwargs={'bid': self.art.id}))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['pre_id'], self.art.id)
        self.assertEqual(pagination['next_id'], self.art.id)
        self.assertEqual(pagination['pre_title'], '')
        self.assertEqual(pagination['next_title'], '')


class TestGetBlog(TestCase):
    def setUp(self):
        self.classify = Classification.objects.create(c_name='test')
        self.tag = Tag.objects.create(tag_name='test')
        self.art = Article.objects.create(caption='article',
                                          sub_caption='sub_article',
                                          classification=self.classify,
                                          content='article test',
                                          publish=True)
        self.art.tags.add(self.tag)
        self.art.save()

    def test_get_blog(self):
        resp = self.client.get(reverse('blog_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        self.assertEqual(res_json['status'], 1)

    def test_pagnination(self):
        resp = self.client.get(reverse('blog_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        pagination = res_json['body']['pagination']
        self.assertEqual(pagination['page'], 1)
        self.assertEqual(pagination['total_page'], 1)
        self.assertEqual(pagination['total'], 1)
        self.assertEqual(pagination['pre'], 0)
        self.assertEqual(pagination['next'], 0)


class TestGetTools(TestCase):
    def setUp(self):
        self.classify = Classification.objects.create(c_name='test')
        self.tag = Tag.objects.create(tag_name='test')
        self.art = Article.objects.create(caption='article',
                                          sub_caption='sub_article',
                                          classification=self.classify,
                                          content='article test',
                                          publish=True)
        self.art.tags.add(self.tag)
        self.art.save()

    def test_get_tools(self):
        resp = self.client.get(reverse('tools_json'))
        self.assertEqual(resp.status_code, 200)
        res_json = json.loads(resp.content)
        res = res_json['body']
        self.assertEqual(res_json['status'], 1)
        self.assertEqual(res['latest_list'][0]['caption'], 'article')
        self.assertEqual(res['classify_list'][0]['c_name'], 'test')
        self.assertEqual(res['read_list'][0]['caption'], 'article')