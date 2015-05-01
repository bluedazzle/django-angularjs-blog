# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20150427_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='publish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
