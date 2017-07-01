# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], max_length=20)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
