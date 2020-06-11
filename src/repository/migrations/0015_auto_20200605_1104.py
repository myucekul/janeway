# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-05 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0021_auto_20190329_1202'),
        ('repository', '0014_preprintfile_original_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='domain',
            field=models.CharField(default='www.example.com', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='is_secure',
            field=models.BooleanField(default=False, help_text='If the site should redirect to HTTPS, mark this.'),
        ),
        migrations.AddField(
            model_name='repository',
            name='press',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='press.Press'),
            preserve_default=False,
        ),
    ]