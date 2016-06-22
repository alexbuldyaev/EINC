# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('einc', '0003_auto_20160622_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StatName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='policycar',
            name='Status',
            field=models.ForeignKey(to='einc.Status'),
        ),
        migrations.AlterField(
            model_name='policyhome',
            name='Status',
            field=models.ForeignKey(to='einc.Status'),
        ),
    ]
