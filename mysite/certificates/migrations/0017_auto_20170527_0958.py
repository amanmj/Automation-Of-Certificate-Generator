# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0016_auto_20170527_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='latex_template',
            field=models.CharField(max_length=25),
        ),
    ]