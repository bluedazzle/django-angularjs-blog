# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_commentreply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong',
            field=models.ForeignKey(blank=True, to='myblog.Article', null=True),
            preserve_default=True,
        ),
    ]
