# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20150422_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.CharField(default=b'\xe5\x8c\xbf\xe5\x90\x8d\xe7\xbd\x91\xe5\x8f\x8b', max_length=100)),
                ('avatar', models.CharField(default=b'default.png', max_length=300)),
                ('reply', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.CharField(default=b'\xe5\x8c\xbf\xe5\x90\x8d\xe7\xbd\x91\xe5\x8f\x8b', max_length=100)),
                ('avatar', models.CharField(default=b'default.png', max_length=300)),
                ('replyed', models.ForeignKey(related_name='replys', blank=True, to='myblog.Comment', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
