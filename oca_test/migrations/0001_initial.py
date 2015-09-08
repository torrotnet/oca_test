# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('text', models.TextField()),
                ('yes', models.IntegerField()),
                ('no', models.IntegerField()),
                ('do_not_know', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(choices=[('1', '14-18'), ('2', '18+')], max_length=1)),
                ('sex', models.CharField(choices=[('1', 'female'), ('2', 'male')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to='oca_test.User', serialize=False)),
                ('A', models.IntegerField()),
                ('B', models.IntegerField()),
                ('C', models.IntegerField()),
                ('D', models.IntegerField()),
                ('E', models.IntegerField()),
                ('F', models.IntegerField()),
                ('G', models.IntegerField()),
                ('H', models.IntegerField()),
                ('I', models.IntegerField()),
                ('J', models.IntegerField()),
            ],
        ),
    ]
