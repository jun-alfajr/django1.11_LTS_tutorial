# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180904_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
