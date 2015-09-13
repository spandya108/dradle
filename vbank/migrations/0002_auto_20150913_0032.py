# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vbank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('credit', models.IntegerField(default=0)),
                ('debit', models.IntegerField(default=0)),
                ('combined', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=None, blank=True)),
                ('month', models.DateField(default=None, blank=True)),
                ('type', models.CharField(default=b'', max_length=100, blank=True)),
                ('bank', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserBank',
        ),
    ]
