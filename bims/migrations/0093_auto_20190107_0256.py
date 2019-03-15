# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-07 02:56
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0092_fbisuuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=b''),
        ),
        migrations.AddField(
            model_name='profile',
            name='fbis_username',
            field=models.CharField(blank=True, default=b'', max_length=150),
        ),
    ]
