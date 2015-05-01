# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wmd.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20150424_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifycode',
            name='description',
            field=wmd.models.MarkDownField(default=datetime.datetime(2015, 4, 26, 3, 46, 1, 414052, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
