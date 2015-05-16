# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from app.blog_lab.proxy.method import get_proxy


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_proxy()