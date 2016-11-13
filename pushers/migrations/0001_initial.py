# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buggy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BuggyRoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buggy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pushers.Buggy')),
            ],
        ),
        migrations.CreateModel(
            name='Pusher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RollHill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hill', models.PositiveIntegerField()),
                ('pusher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pushers.Pusher')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pushers.BuggyRoll')),
            ],
        ),
        migrations.CreateModel(
            name='RollsDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('active_pushers', models.ManyToManyField(to='pushers.Pusher')),
            ],
        ),
        migrations.AddField(
            model_name='roll',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pushers.RollsDay'),
        ),
        migrations.AddField(
            model_name='buggyroll',
            name='roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pushers.Roll'),
        ),
    ]
