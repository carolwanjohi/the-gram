# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]