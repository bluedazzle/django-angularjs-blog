# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20150426_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='env',
            field=models.ManyToManyField(related_name='knowledges', null=True, to='myblog.Env', blank=True),
            preserve_default=True,
        ),
    ]
