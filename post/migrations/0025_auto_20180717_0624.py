# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-17 06:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20180713_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.Post'),
        ),
    ]
