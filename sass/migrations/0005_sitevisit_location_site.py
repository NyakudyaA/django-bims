# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0100_auto_20190109_0645'),
        ('sass', '0004_auto_20190109_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitevisit',
            name='location_site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bims.LocationSite'),
        ),
    ]
