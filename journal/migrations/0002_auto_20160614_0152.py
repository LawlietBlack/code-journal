# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='resources',
        ),
        migrations.AddField(
            model_name='resource',
            name='entry',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='journal.Entry'),
            preserve_default=False,
        ),
    ]