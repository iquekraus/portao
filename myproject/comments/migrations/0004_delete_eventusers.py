# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-07 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_eventusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventUsers',
        ),
    ]
