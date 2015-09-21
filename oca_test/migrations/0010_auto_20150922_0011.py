# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0009_results_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='id',
            field=models.IntegerField(serialize=False, default=1, primary_key=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='user',
            field=models.ForeignKey(to='oca_test.User'),
        ),
    ]
