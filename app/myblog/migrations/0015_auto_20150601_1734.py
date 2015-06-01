# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_delete_verifycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='belong',
            field=models.ForeignKey(related_name='comments', to='myblog.Article'),
            preserve_default=True,
        ),
    ]
