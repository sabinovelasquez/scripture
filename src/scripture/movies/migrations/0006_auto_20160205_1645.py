# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20160205_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sequences', to='movies.Movie'),
        ),
    ]
