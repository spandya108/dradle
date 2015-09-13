# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vbank', '0003_auto_20150913_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('credit', models.IntegerField(default=0)),
                ('debit', models.IntegerField(default=0)),
                ('combined', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=None, blank=True)),
                ('month', models.DateField(default=None, blank=True)),
                ('type', models.CharField(default=b'', max_length=100, blank=True)),
                ('institution', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='bank',
            new_name='institution',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='virtual_txn',
            new_name='v_transaction',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='virtual',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
    ]
