# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20160614_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
