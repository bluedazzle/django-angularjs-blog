from django.views.generic import DetailView, CreateView
from django.utils import timezone
from django.http import HttpResponse

import simplejson

from app.utils import model_serializer
from app.myblog.models import Article

class ArticleDetailView(DetailView):
    model = Article
    queryset = Article.objects
    slug_url_kwarg = '11'
    slug_field = 'id'
    template_name = 'test_cbv.html'
    http_method_names = [u'get', u'post', u'put', u'patch', u'delete', u'head', u'options', u'trace', u'link']


    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_object(self, queryset=None):
        return Article.objects.get(id=11)

    # def get(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     json_obj = model_serializer(obj, serializer='json')
    #     return HttpResponse(json_obj, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('delete')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')

    def link(self, request, *args, **kwargs):
        return HttpResponse('link')




