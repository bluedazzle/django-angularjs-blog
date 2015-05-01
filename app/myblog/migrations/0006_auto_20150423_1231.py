# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_comment_belong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='belong',
            field=models.ForeignKey(default=1, to='myblog.Article'),
            preserve_default=False,
        ),
    ]
