# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 12:15
from __future__ import unicode_literals

import bims.enums.taxonomic_rank
import bims.enums.taxonomic_status
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0070_remove_biologicalcollectionrecord_endemism'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxonIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gbif_key', models.IntegerField(blank=True, null=True, verbose_name=b'GBIF Key')),
                ('scientific_name', models.CharField(max_length=100, verbose_name=b'Scientific Name')),
                ('canonical_name', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Canonical Name')),
                ('description', models.TextField(blank=True, default=b'', verbose_name=b'Description')),
                ('rank', models.CharField(blank=True, choices=[(bims.enums.taxonomic_rank.TaxonomicRank(b'Class'), b'Class'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Domain'), b'Domain'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Family'), b'Family'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Genus'), b'Genus'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Kingdom'), b'Kingdom'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Life'), b'Life'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Order'), b'Order'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Phylum'), b'Phylum'), (bims.enums.taxonomic_rank.TaxonomicRank(b'Species'), b'Species')], max_length=50, verbose_name=b'Taxonomic Rank')),
                ('vernacular_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=b'', max_length=100), blank=True, default=[], null=True, size=None, verbose_name=b'Vernacular Names')),
                ('taxonomic_status', models.CharField(blank=True, choices=[(bims.enums.taxonomic_status.TaxonomicStatus(b'Accepted'), b'Accepted'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Doubtful'), b'Doubtful'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Heterotypic Synonym'), b'Heterotypic Synonym'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Homotypic Synonym'), b'Homotypic Synonym'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Misapplied'), b'Misapplied'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Proparte Synonym'), b'Proparte Synonym'), (bims.enums.taxonomic_status.TaxonomicStatus(b'Synonym'), b'Synonym')], max_length=50, verbose_name=b'Taxonomic Status')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bims.TaxonIdentifier', verbose_name=b'Parent')),
            ],
        ),
    ]