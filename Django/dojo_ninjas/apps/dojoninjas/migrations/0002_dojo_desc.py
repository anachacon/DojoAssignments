# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-16 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='No description'),
        ),
    ]
