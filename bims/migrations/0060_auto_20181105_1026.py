# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-05 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0059_merge_20181105_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationsite',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='locationsite',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
