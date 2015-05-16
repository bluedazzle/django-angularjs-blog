#!encoding=utf-8
from django.contrib.sitemaps import Sitemap

from app.myblog.models import Article, Knowledge


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Article.objects.filter(publish=True)

    def lastmod(self, item):
        return item.modify_time

    def location(self, item):
        return r'/blog/%d/' % item.id


class KnowSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Knowledge.objects.filter(publish=True)

    def lastmod(self, item):
        return item.modify_time

    def location(self, item):
        return r'/know/'


# class StaticViewSitemap(Sitemap):
    # priority = 0.5
    # changefreq = 'daily'
    #
    # def items(self):
    #     return ['code', 'me']
    #
    # def location(self, item):
    #     return reverse(item)
