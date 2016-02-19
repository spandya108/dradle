# -*- coding: utf-8 -*-
from django.db import models, migrations
import uuid


class Migration(migrations.Migration):
    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=None, blank=True)),
                ('month', models.DateTimeField(default=None, blank=True)),
                ('type', models.CharField(default=b'', max_length=100, blank=True)),
                ('institution', models.CharField(default=b'', max_length=100, blank=True)),
                ('label', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
