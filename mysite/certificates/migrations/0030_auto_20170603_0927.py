# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 09:27
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0029_merge_20170603_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='template',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='certificate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='certificates.Certificate'),
        ),
    ]
