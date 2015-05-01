# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20150423_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modify_time', models.DateTimeField(auto_now_add=True)),
                ('verify', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='env',
            field=models.ManyToManyField(related_name='knowledges', to='myblog.Env'),
            preserve_default=True,
        ),
    ]
