# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_schools'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post', models.TextField()),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
