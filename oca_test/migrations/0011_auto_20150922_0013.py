# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0010_auto_20150922_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),
        ),
    ]
