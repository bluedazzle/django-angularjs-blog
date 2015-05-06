import os
import uwsgi
from app.blog_lab.proxy.method import get_proxy, check_proxy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewRaPo.settings.produce")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

uwsgi.register_signal(82, "", get_proxy)
uwsgi.add_cron(82, 0, -1, -1, -1, -1)
uwsgi.register_signal(84, "", check_proxy)
uwsgi.add_cron(84, 30, -1, -1, -1, -1)