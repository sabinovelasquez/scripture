# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.DateTimeField(verbose_name='released')),
                ('pub_date', models.DateTimeField(verbose_name='published')),
                ('director', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act', models.CharField(max_length=10)),
                ('sequence', models.CharField(max_length=140)),
                ('image', models.FileField(upload_to='img/')),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
    ]
