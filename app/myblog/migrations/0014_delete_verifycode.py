# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_knowledge_publish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VerifyCode',
        ),
    ]
