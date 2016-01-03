# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_auto_20160103_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(choices=[(b'management', b'management'), (b'rnd', b'rnd'), (b'operations', b'operations')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='designation',
            name='managementRank',
        ),
        migrations.RemoveField(
            model_name='designation',
            name='operationsRank',
        ),
        migrations.RemoveField(
            model_name='designation',
            name='rndRank',
        ),
        migrations.AlterField(
            model_name='designation',
            name='rank',
            field=models.ForeignKey(max_length=8, null=True, on_delete=django.db.models.deletion.CASCADE, to='HR.rank'),
        ),
    ]
