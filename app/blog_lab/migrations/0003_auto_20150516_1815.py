# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_lab', '0002_proxyuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proxy',
            name='ip',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
