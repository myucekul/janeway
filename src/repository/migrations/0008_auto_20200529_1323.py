# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20200529_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email_address',
            field=models.EmailField(default=' ', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]