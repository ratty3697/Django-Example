# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.CharField(default=datetime.datetime(2016, 3, 15, 11, 54, 18, 274896, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]