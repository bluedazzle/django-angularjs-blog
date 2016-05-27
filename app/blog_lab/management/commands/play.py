# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from app.myblog.models import Article
from django.db.models import Count, StdDev
from dss import Serializer
from app.blog_lab.proxy.huiyuan import play
from app.myblog.models import Classification, Article

class Command(BaseCommand):

    def handle(self, *args, **options):
        # art_list = Article.objects.all()
        # # for itm in art_list:
        #     # print itm.caption__max
        # print Serializer.serializer(art_list, except_attr=('content', 'caption', 'classification', 'publish'))
        # play()
        # cl = Classification.objects.all()[0]
        # cc = cl.cls_art.all()
        # for i in cc:
        #     i['test'] = 1
        article = Article.objects.distinct('classification__c_name')
        print article