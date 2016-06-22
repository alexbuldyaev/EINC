# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('einc', '0004_auto_20160622_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policycar',
            name='CarDate',
        ),
        migrations.RemoveField(
            model_name='policycar',
            name='CarDocDate',
        ),
    ]
