# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20180215_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'post_image'),
        ),
    ]