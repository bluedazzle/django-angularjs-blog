from django.conf.urls import patterns, url

from app.blog_admin import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='admin_index'),
    url(r'^blog_admin/$', views.blog, name='admin_blog'),
    url(r'^know_admin/$', views.know_admin, name='admin_know'),
    url(r'^create_know/$', views.know, name='admin_new_know'),
    url(r'^create_blog/$', views.create_blog, name='admin_new_blog'),
    url(r'^create_know/(?P<kid>(\d)+)/$', views.know, name='admin_modify_know'),
    url(r'^create_blog/(?P<bid>(\d)+)/$', views.create_blog, name='admin_modify_blog'),

    url(r'^login/$', views.login, name='admin_login'),
    url(r'^know/$', views.know, name='admin_know_json'),
    url(r'^blog_util/$', views.get_blog_util, name='admin_blog_util_json'),
    url(r'^blog_util/(?P<bid>(\d)+)/$', views.get_blog_util, name='admin_modify_blog_util_json'),
    url(r'^new_blog/$', views.new_blog, name='admin_new_blog_json'),
    url(r'^new_tag/$', views.new_tag, name='admin_new_tag_json'),
    url(r'^new_classify/$', views.new_classify, name='admin_new_classify_json'),
    url(r'^new_env/$', views.new_env, name='admin_new_env_json'),
    url(r'^new_know/$', views.new_know, name='admin_new_know_json'),
    url(r'^get_env/$', views.get_env, name='admin_env_json'),
    url(r'^get_env/e/$', views.get_env, name='admin_modify_env_json'),
    url(r'^know_list/$', views.know_list, name='admin_know_list_json'),
    url(r'^comment_list/$', views.comment_list, name='admin_comment_list_json'),
    url(r'^comment_admin/$', views.comment_admin, name='admin_comment_json'),
    url(r'^blog_list/$', views.blog_list, name='admin_blog_list_json'),
    url(r'^blog_opt/$', views.blog_opt, name='admin_blog_opt_json'),
    url(r'^know_opt/$', views.know_opt, name='admin_know_opt_json'),
    url(r'^comment_opt_del/$', views.comment_opt_del, name='admin_comment_opt_json'),
    url(r'^comment_opt_new/$', views.comment_opt_new, name='admin_comment_opt_new_json'),
)
