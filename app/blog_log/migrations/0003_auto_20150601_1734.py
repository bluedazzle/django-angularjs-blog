# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_log', '0002_backlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='fail_message',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
    ]
