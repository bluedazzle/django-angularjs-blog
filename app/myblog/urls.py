from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.myblog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewRaPo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^blog$', views.blog),
    url(r'^blog/comment/(?P<bid>(.*)+)/$', views.submit_comment),
    url(r'^blog/(?P<bid>(.*)+)/$', views.blog),
    url(r'^knowledge$', views.know),
    url(r'^me$', views.about),
    url(r'^get_knowledge/(?P<text>(.*)+)/$', views.get_know),
    url(r'^get_knowledge$', views.get_know),
    url(r'^detail$', views.detail),
    url(r'^tools$', views.get_tools),
    url(r'^detail/(?P<bid>\d+)/$', views.detail),
    url(r'^bd$', views.get_blog),
    url(r'^refresh_verify$', views.refresh_verify),
    url(r'^code$', views.code),
    url(r'^lab$', views.lab),
    url(r'^tag/(?P<bid>(.*)+)/$', views.tag),
    url(r'^get_tag/(?P<tid>(.*)+)/$', views.get_tag),
    url(r'^classify/(?P<bid>(.*)+)/$', views.classify),
    url(r'^get_classify/(?P<cid>(.*)+)/$', views.get_classify),
    url(r'^index_content$', views.get_index),
)
