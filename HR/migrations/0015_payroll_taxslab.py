# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0014_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='taxSlab',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
