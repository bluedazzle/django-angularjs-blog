# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_verifycode_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags_art', null=True, to='myblog.Tag', blank=True),
            preserve_default=True,
        ),
    ]
