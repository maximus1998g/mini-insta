# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20180214_1126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]