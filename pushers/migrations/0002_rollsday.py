# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pushers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollsDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
