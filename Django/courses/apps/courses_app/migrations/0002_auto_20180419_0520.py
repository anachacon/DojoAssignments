# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-19 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='last_name',
            new_name='desc',
        ),
    ]
