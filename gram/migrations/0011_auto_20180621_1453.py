# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0010_auto_20180621_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('post_date',)},
        ),
    ]