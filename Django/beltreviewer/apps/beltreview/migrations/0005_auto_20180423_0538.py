# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0004_auto_20180423_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author',
        ),
    ]