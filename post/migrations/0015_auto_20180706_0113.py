# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-06 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20180215_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments_from',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comments_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comments_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='like_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='like_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name=b'post_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name=b'post_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_text',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(default=datetime.datetime(2018, 7, 6, 1, 13, 40, 692701, tzinfo=utc), verbose_name='T\u0435\u043a\u0441\u0442 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('post', 'author')]),
        ),
    ]