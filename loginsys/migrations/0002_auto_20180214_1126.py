# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile222',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile222',
        ),
    ]
