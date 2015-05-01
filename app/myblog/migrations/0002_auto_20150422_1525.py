# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 25, 0, 378762), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 22, 15, 25, 20, 354135), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(related_name='cls_art', to='myblog.Classification'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags_art', to='myblog.Tag', blank=True),
            preserve_default=True,
        ),
    ]
