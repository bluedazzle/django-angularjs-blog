# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_comment_commentreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='to',
            field=models.CharField(default=b'\xe5\x8c\xbf\xe5\x90\x8d\xe7\xbd\x91\xe5\x8f\x8b', max_length=100),
            preserve_default=True,
        ),
    ]
