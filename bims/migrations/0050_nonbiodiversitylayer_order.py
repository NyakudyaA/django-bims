# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-15 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0049_auto_20181011_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonbiodiversitylayer',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]