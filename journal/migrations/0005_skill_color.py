# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_skill_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='color',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
