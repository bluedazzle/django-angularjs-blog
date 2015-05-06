# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=64)),
                ('ip', models.CharField(max_length=20)),
                ('record', models.CharField(default=b'', max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
