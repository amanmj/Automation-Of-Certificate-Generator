# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0027_auto_20170603_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercertificateinfo',
            name='qrcode',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
