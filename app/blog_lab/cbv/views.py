# coding:utf-8
from __future__ import unicode_literals

from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.http.response import HttpResponse
from django.utils import timezone
from django.http import HttpResponse
import datetime
import ujson
import json
from app.myblog.models import Article
from src.dss.Mixin import *
from src.dss.Serializer import *

def test(req):
    article_list = Article.objects.all()
    article = article_list[0]
    # print article._meta.get_all_field_names()
    # print getattr(article, 'tags').all()[0].tags_art.all()
    json_data = serializer(article, datetime_format='timestamp', output_type='json', deep=True, many=True, exclude_attr=['comments','tags'])
    return HttpResponse(json_data, content_type='application/json')


class ArticleDetailView(JsonResponseMixin, DetailView):
    model = Article
    datetime_type = 'timestamp'
    many = True
    foreign = True
    exclude_attr = ('comments', )
    fields = ['caption', 'content', 'classification', 'tags']
    queryset = Article.objects.all()
    # slug_url_kwarg = '32'
    pk_url_kwarg = 'id'
    success_url = '/'
    # context_object_name = 'article_list'
    # queryset = Article.objects.filter(publish=False)
    # ordering = '-create_time'
    # paginate_orphans = 1
    paginate_by = 2
    # slug_field = 'id'
    template_name = 'test_cbv.html'
    # http_method_names = [u'get', u'post', u'put', u'patch', u'delete', u'head', u'options', u'trace', u'link']


    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        print context
        # print context['page_obj'].paginator.page_range
        return context
    #
    # # def get_object(self, queryset=None):
    # #     return Article.objects.get(id=32)
    #
    # def get(self, request, *args, **kwargs):
    #     self.kwargs['id'] = u'32'
    #     return super(ArticleDetailView, self).get(request, *args, **kwargs)
        #
        # # def get(self, request, *args, **kwargs):
        # #     obj = self.get_object()
        # #     json_obj = model_serializer(obj, serializer='json')
        # #     return HttpResponse(json_obj, content_type='application/json')
        #
        # def delete(self, request, *args, **kwargs):
        #     return HttpResponse('delete')
        #
        # def post(self, request, *args, **kwargs):
        #     return HttpResponse('post')
        #
        # def link(self, request, *args, **kwargs):
        #     return HttpResponse('link')




