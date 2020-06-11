# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-04 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0012_auto_20200602_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='limit_upload_to_pdf',
            field=models.BooleanField(default=False, help_text='If set to True, this will require all file uploads fromauthors to be PDF files.'),
        ),
        migrations.AlterField(
            model_name='author',
            name='orcid',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ORCID'),
        ),
    ]