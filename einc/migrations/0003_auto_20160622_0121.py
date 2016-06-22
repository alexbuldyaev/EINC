# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('einc', '0002_auto_20160521_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TypeName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='policycar',
            name='PolicyType',
            field=models.ForeignKey(to='einc.PolicyType'),
        ),
        migrations.AlterField(
            model_name='policyhome',
            name='PolicyType',
            field=models.ForeignKey(to='einc.PolicyType'),
        ),
    ]
