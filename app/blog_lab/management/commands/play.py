# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from app.myblog.models import Article
from django.db.models import Count, StdDev
from dss import Serializer
from app.blog_lab.proxy.huiyuan import play

class Command(BaseCommand):

    def handle(self, *args, **options):
        # art_list = Article.objects.all()
        # # for itm in art_list:
        #     # print itm.caption__max
        # print Serializer.serializer(art_list, except_attr=('content', 'caption', 'classification', 'publish'))
        play()
