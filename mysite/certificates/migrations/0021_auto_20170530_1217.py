# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 19:17
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0020_auto_20170530_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='template',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='media'),
        ),
    ]
