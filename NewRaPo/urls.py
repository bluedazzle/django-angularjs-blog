from django.conf.urls import patterns, include, url
from django.contrib import admin

from NewRaPo.settings import base as settings
from NewRaPo.sitemaps import BlogSitemap, KnowSitemap


sitemaps = {
    'blog': BlogSitemap,
    # 'static': StaticViewSitemap,
    'knowledge': KnowSitemap
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewRaPo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app.myblog.urls')),
    url(r'^blog_admin/', include('app.blog_admin.urls')),
    url(r'^lab/', include('app.blog_lab.urls')),
    # url(r'404', 'app.myblog.views.not_found'),
    # url(r'500', 'app.myblog.views.server_error'),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CSS_DIR}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.JS_DIR}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMG_DIR}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.FONTS_DIR}),
    url(r'^verify/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.VERIFY_DIR}),
    url(r'^file/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.FILE_DIR}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR}),
)
