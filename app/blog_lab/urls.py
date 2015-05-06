from django.conf.urls import patterns, include, url
from app.blog_lab.proxy import views
from app.blog_lab.views import *


urlpatterns = patterns('',
    url(r'^create_token$', views.create_permission),
    url(r'^get_proxy$', views.get_ip),
    url(r'^proxy/$', proxy),
    url(r'^get_proxy_info/$', get_proxy_info),
    )