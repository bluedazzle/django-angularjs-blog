from django.test import TestCase

from app.myblog.models import Tag, Classification, Article


class TestEnv(TestCase):

    def _getTarget(self):
        from app.myblog.models import Env
        return Env

    def _createOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_create(self):
        new_env = self._createOne()
        self.assertEqual(new_env.content, '')

    def test_set_value(self):
        new_env = self._createOne()
        new_env.content = 'test'
        self.assertEqual(new_env.content, 'test')


class TestArticle(TestCase):

    def setUp(self):
        tag = Tag.objects.create(tag_name='test')
        classify = Classification.objects.create(c_name='test')
        art = Article.objects.create(caption='article',
                               sub_caption='sub_article',
                               classification=classify,
                               content='article test')
        art.tags.add(tag)
        art.save()
        art1 = Article.objects.create(caption='article1',
                               sub_caption='sub_article',
                               classification=classify,
                               content='article test')
        art1.tags.add(tag)
        art1.save()

    def test_create(self):
        new_art = Article.objects.get(caption='article')
        tag = Tag.objects.get(tag_name='test')
        classify = Classification.objects.get(c_name='test')
        self.assertEqual(new_art.content, 'article test')
        self.assertEqual(new_art.caption, 'article')
        self.assertEqual(new_art.publish, False)
        self.assertEqual(new_art.sub_caption, 'sub_article')
        self.assertEqual(new_art.read_count, 0)
        self.assertEqual(new_art.comment_count, 0)
        self.assertEqual(new_art.classification, classify)

    def test_serializer(self):
        art = Article.objects.get(caption='article')
        serializ = art.serializer()
        self.assertIsInstance(serializ, dict)
        self.assertEqual(serializ['caption'], 'article')
        self.assertIsInstance(serializ['create_time'], float)
        self.assertNotIn('classification', serializ)

    def test_serializer_deep(self):
        art = Article.objects.get(caption='article')
        serializ = art.serializer(deep=True)
        self.assertIn('classification', serializ)

    def test_serializer_time_format(self):
        art = Article.objects.get(caption='article')
        serializ = art.serializer(time_format="string")
        self.assertIsInstance(serializ['create_time'], str)
        serializ = art.serializer(time_format="utc")
        self.assertIsInstance(serializ['create_time'], str)





