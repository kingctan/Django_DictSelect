# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.IntegerField(default=0, verbose_name='\u5e8f\u53f7')),
                ('dictname', models.CharField(max_length=50, verbose_name='\u5b57\u5178\u540d')),
                ('dictcode', models.CharField(max_length=50, verbose_name='\u5b57\u5178\u7f16\u7801')),
            ],
            options={
                'ordering': ['seq'],
                'db_table': 't_s_dict',
                'verbose_name': '\u5b57\u5178\u9879',
                'verbose_name_plural': '\u5b57\u5178\u9879',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.IntegerField(default=0, verbose_name='\u5e8f\u53f7')),
                ('itemcode', models.CharField(max_length=50, verbose_name='\u5b57\u5178\u7f16\u7801')),
                ('itemname', models.CharField(max_length=50, verbose_name='\u5b57\u5178\u540d')),
                ('dictgroup', models.ForeignKey(to='DataDict.Dict')),
            ],
            options={
                'ordering': ['seq'],
                'db_table': 't_s_item',
                'verbose_name': '\u5b57\u5178\u503c',
                'verbose_name_plural': '\u5b57\u5178\u503c',
            },
            bases=(models.Model,),
        ),
    ]
