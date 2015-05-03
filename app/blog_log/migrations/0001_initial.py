# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(unique=True, max_length=20)),
                ('belong', models.CharField(max_length=50)),
                ('total', models.IntegerField(default=0)),
                ('day_count', models.IntegerField(default=0)),
                ('black', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReqRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('uri', models.CharField(default=b'', max_length=100)),
                ('ip', models.ForeignKey(related_name='records', to='blog_log.AccIP')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
