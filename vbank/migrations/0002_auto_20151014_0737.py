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
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('safe_to_spend', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='vbank.Category', null=True),
        ),
        migrations.AlterField(
            model_name='physicaltransaction',
            name='month',
            field=models.DateTimeField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='virtualtransaction',
            name='month',
            field=models.DateTimeField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='physicaltransaction',
            name='user',
            field=models.ForeignKey(to='vbank.User', null=True),
        ),
        migrations.AddField(
            model_name='virtualtransaction',
            name='user',
            field=models.ForeignKey(to='vbank.User', null=True),
        ),
    ]
