from django.test import TestCase
from django.utils.timezone import get_current_timezone

from app.utils import *
from app.myblog.models import Article, Classification


class TestEncodeJson(TestCase):
    def test_ecnode(self):
        res = encodejson(1, {})
        self.assertIsInstance(res ,str)


class TestCreateRandom(TestCase):
    def test_create(self):
        res = create_random_str(10)
        self.assertEqual(len(res), 10)
        res = create_random_str(62)
        self.assertEqual(len(res), 62)
        res = create_random_str(63)
        self.assertEqual(res, 'too long str')

    def test_format(self):
        res = create_random_str(60)
        for itm in ['+', '-', '_', '=', '|', '!', '?', '`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
            self.assertNotIn(itm, res)


class TestString2Datetime(TestCase):
    def test_convert(self):
        sample = '2011-1-1 19:25:01'
        res = string_to_datetime(sample)
        self.assertIsInstance(res, datetime.datetime)
        self.assertEqual(res.second, 1)
        self.assertEqual(res.minute, 25)
        self.assertEqual(res.hour, 19)
        self.assertEqual(res.day, 1)
        self.assertEqual(res.month, 1)
        self.assertEqual(res.year, 2011)

    def test_format(self):
        sample = '2015/1/1 23-12-11'
        format_str = '%Y/%m/%d %H-%M-%S'
        res = string_to_datetime(sample, format_str)
        self.assertIsInstance(res, datetime.datetime)


class TestDatetime2Timestamp(TestCase):
    def test_convert(self):
        sample = datetime.datetime.now()
        res = datetime_to_timestamp(sample)
        self.assertIsInstance(res, float)
        sample.replace(tzinfo=get_current_timezone())
        res = datetime_to_timestamp(sample)
        self.assertIsInstance(res, float)


class TestDatetime2String(TestCase):
    def test_convert(self):
        sample = string_to_datetime('2011-1-1 19:25:01')
        res = datetime_to_string(sample)
        self.assertEqual(res, '2011-01-01 19:25:01')
        sample.replace(tzinfo=get_current_timezone())
        res = datetime_to_string(sample)
        self.assertEqual(res, '2011-01-01 19:25:01')


class TestDatetime2UtcString(TestCase):
    def test_convert(self):
        sample = string_to_datetime('2011-1-1 19:25:01')
        res = datetime_to_utc_string(sample)
        self.assertEqual(res, '2011-01-01 19:25:01+08:00')


class TestModeSerializer(TestCase):
    def setUp(self):
        classify = Classification.objects.create(c_name='test')
        art = Article.objects.create(caption='article',
                               sub_caption='sub_article',
                               classification=classify,
                               content='article test')
        art1 = Article.objects.create(caption='article1',
                               sub_caption='sub_article',
                               classification=classify,
                               content='article test')

    def test_serializer(self):
        art = Article.objects.get(caption='article')
        serial = model_serializer(art)
        self.assertIsInstance(serial, dict)
        serial = model_serializer(art, serializer='json')
        self.assertIsInstance(serial, str)
        serial = model_serializer(art, serializer='xml')
        self.assertIn('xml version="1.0', serial)

    def test_serializer_list(self):
        art_list = Article.objects.all()
        serial = model_serializer(art_list)
        self.assertIsInstance(serial, list)
        serial = model_serializer(art_list, serializer='json')
        self.assertIsInstance(serial, str)

    def test_include(self):
        art = Article.objects.get(caption='article')
        serial = model_serializer(art, include_attr=['caption', 'content'])
        self.assertIn('caption', serial)
        self.assertNotIn('create_time', serial)

    def test_except(self):
        art = Article.objects.get(caption='article')
        serial = model_serializer(art, except_attr=['caption', 'content'])
        self.assertNotIn('caption', serial)
        self.assertIn('create_time', serial)

    def test_include_except(self):
        art = Article.objects.get(caption='article')
        serial = model_serializer(art, include_attr=['caption', 'content'], except_attr=['content'])
        self.assertIn('caption', serial)
        self.assertNotIn('content', serial)


class TestCreateVerifyPic(TestCase):
    def test_create(self):
        img, code = create_verify_code()
        self.assertIsInstance(img, str)
        self.assertIsInstance(code, str)
