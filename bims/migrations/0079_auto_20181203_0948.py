# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0078_auto_20181203_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxongroup',
            old_name='taxon_identifiers',
            new_name='taxonomies',
        ),
    ]
