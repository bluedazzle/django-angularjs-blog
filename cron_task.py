"""
WSGI config for NewRaPo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

import uwsgi
from app.blog_lab.proxy.method import get_proxy, check_proxy
from app.blog_lab.proxy.huiyuan import play

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewRaPo.settings.produce")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

uwsgi.register_signal(82, "", get_proxy)
uwsgi.add_cron(82, 0, -1, -1, -1, -1)
uwsgi.register_signal(84, "", check_proxy)
uwsgi.add_cron(84, 30, -1, -1, -1, -1)
uwsgi.register_signal(86, "", play)
uwsgi.add_cron(86, 0, 8, -1, -1, -1)