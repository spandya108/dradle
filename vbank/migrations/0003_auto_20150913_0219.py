# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vbank', '0002_auto_20150913_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='virtual_txn',
            field=models.ForeignKey(blank=True, to='vbank.Transaction', null=True),
        ),
    ]
