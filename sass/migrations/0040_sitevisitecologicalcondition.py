# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sass', '0039_delete_samplingmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisitEcologicalCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sass_score', models.IntegerField(blank=True, null=True)),
                ('aspt_score', models.FloatField(blank=True, null=True)),
                ('ecological_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sass.SassEcologicalCategory')),
                ('site_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sass.SiteVisit')),
            ],
        ),
    ]
