from django.conf.urls import patterns, url

from app.myblog import views


urlpatterns = patterns('',
    #django url
    url(r'^$', views.index, name='index'),
    url(r'^code/$', views.code, name='code'),
    url(r'^lab/$', views.lab, name='lab'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^knowledge/$', views.know, name='know'),
    url(r'^me/$', views.about, name='about'),
    url(r'^classify/(?P<bid>(\d)+)/$', views.classify, name='classify'),
    url(r'^blog/(?P<bid>(\d)+)/$', views.blog, name='blog_with_id'),
    url(r'^tag/(?P<bid>(\d)+)/$', views.tag, name='tag'),

    #json url
    url(r'^blog/comment/(?P<bid>(.*)+)/$', views.submit_comment, name='submit_comment'),
    url(r'^get_knowledge/(?P<text>(.*)+)/$', views.get_know, name='know_json_text'),
    url(r'^get_knowledge/$', views.get_know, name='know_json'),
    url(r'^detail/$', views.detail, name='detail_json'),
    url(r'^tools/$', views.get_tools, name='tools_json'),
    url(r'^detail/(?P<bid>\d+)/$', views.detail, name='detail_json_id'),
    url(r'^bd/$', views.get_blog, name='blog_json'),
    url(r'^refresh_verify/$', views.refresh_verify, name='verify_json'),
    url(r'^get_tag/(?P<tid>(.*)+)/$', views.get_tag, name='tag_json'),
    url(r'^get_classify/(?P<cid>(.*)+)/$', views.get_classify, name='classify_json'),
    url(r'^index_content/$', views.get_index, name='index_json'),
    url(r'^migrate/$', views.migrate_blog),
    url(r'^knows/$', views.migrate_knows),
)
