# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20150423_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('env', models.ManyToManyField(to='myblog.Env')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='classification',
            name='c_name',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
