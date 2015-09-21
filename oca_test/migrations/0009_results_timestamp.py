# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oca_test', '0008_auto_20150915_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
