# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='photo',
            field=models.ImageField(default=0, upload_to='%Y/%m/%d/photos/'),
            preserve_default=False,
        ),
    ]
