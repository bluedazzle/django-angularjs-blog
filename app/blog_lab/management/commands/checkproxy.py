# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from app.blog_lab.proxy.method import check_proxy
from app.blog_lab.models import Proxy


class Command(BaseCommand):
    def handle(self, *args, **options):
        check_proxy()