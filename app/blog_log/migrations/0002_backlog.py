# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=50)),
                ('log_type', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('fail_message', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
