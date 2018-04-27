# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import organization.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=400)),
                ('mobile', models.PositiveIntegerField()),
                ('telephone', models.PositiveIntegerField(default=0, null=True)),
                ('fax', models.PositiveIntegerField(default=0, null=True)),
                ('picture', models.FileField(null=True, upload_to=organization.models.getDepartmentsLogoAttachmentPath)),
                ('contacts', models.ManyToManyField(related_name='departmentsHeading', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('logo', models.FileField(null=True, upload_to=organization.models.getDivisionLogoAttachmentPath)),
                ('gstin', models.CharField(max_length=200)),
                ('pan', models.CharField(max_length=200)),
                ('cin', models.CharField(max_length=200)),
                ('l1', models.CharField(max_length=200)),
                ('l2', models.CharField(max_length=200)),
                ('contacts', models.ManyToManyField(related_name='divisionsHeading', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='organization.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('pincode', models.PositiveIntegerField()),
                ('l1', models.CharField(max_length=200)),
                ('l2', models.CharField(max_length=200)),
                ('mobile', models.PositiveIntegerField(default=0, null=True)),
                ('telephone', models.PositiveIntegerField(default=0, null=True)),
                ('fax', models.PositiveIntegerField(default=0, null=True)),
                ('contacts', models.ManyToManyField(related_name='unitsHeading', to=settings.AUTH_USER_MODEL)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='organization.Division')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='organization.Units')),
            ],
        ),
        migrations.AddField(
            model_name='departments',
            name='units',
            field=models.ManyToManyField(related_name='departmentsUnits', to='organization.Units'),
        ),
    ]
