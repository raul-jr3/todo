# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/photos/'),
        ),
    ]