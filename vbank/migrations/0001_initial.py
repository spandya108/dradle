# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('remaining', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'New Budget', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'Category', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=b'', blank=True)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'New Goal', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('credit', models.IntegerField(default=0)),
                ('debit', models.IntegerField(default=0)),
                ('combined', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=None, blank=True)),
                ('month', models.DateField(default=None, blank=True)),
                ('type', models.CharField(default=b'', max_length=100, blank=True)),
                ('institution', models.CharField(default=b'', max_length=100, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('budgets', models.ManyToManyField(to='vbank.Budget', blank=True)),
                ('categories', models.ManyToManyField(to='vbank.Category', blank=True)),
                ('goals', models.ManyToManyField(to='vbank.Goal', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('count', models.IntegerField(default=1)),
                ('budgets', models.ManyToManyField(to='vbank.Budget', blank=True)),
                ('categories', models.ManyToManyField(to='vbank.Category', blank=True)),
                ('goals', models.ManyToManyField(to='vbank.Goal', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='physicaltransaction',
            name='v_transaction',
            field=models.ForeignKey(blank=True, to='vbank.VirtualTransaction', null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='p_transactions',
            field=models.ManyToManyField(to='vbank.PhysicalTransaction', blank=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='v_transactions',
            field=models.ManyToManyField(to='vbank.VirtualTransaction', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='p_transactions',
            field=models.ManyToManyField(to='vbank.PhysicalTransaction', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='v_transactions',
            field=models.ManyToManyField(to='vbank.VirtualTransaction', blank=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(to='vbank.Category', null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='p_transactions',
            field=models.ManyToManyField(to='vbank.PhysicalTransaction', blank=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='v_transactions',
            field=models.ManyToManyField(to='vbank.VirtualTransaction', blank=True),
        ),
    ]
