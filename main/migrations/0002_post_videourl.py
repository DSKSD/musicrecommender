# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-07 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videourl',
            field=models.CharField(max_length=300, null=True),
        ),
    ]