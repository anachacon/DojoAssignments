# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0003_auto_20180423_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
