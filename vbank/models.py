from django.db import models
import uuid

# Create your models here.


class Transaction(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    credit          = models.IntegerField(default=0)
    debit           = models.IntegerField(default=0)
    combined        = models.BooleanField(default=False)
    date            = models.DateTimeField(default=None, blank=True)
    month           = models.DateField(default=None, blank=True)
    type            = models.CharField(default='', blank=True, max_length=100)
    institution     = models.CharField(default='', blank=True, max_length=100)
    budgets         = models.ManyToManyField('Budget', blank=True)
    goals           = models.ManyToManyField('Goal', blank=True)
    categories      = models.ManyToManyField('Category', blank=True)
    title           = models.CharField(max_length=100)
    description     = models.TextField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '[-' + credit + '][+' + debit + ']'


class PhysicalTransaction(Transaction):

    v_transaction   = models.ForeignKey('VirtualTransaction', null=True, blank=True)


class VirtualTransaction(Transaction):

    name            = models.CharField(null=False, max_length=100)
    count           = models.IntegerField(default=1)


class Budget(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount          = models.IntegerField(default=0)
    remaining       = models.IntegerField(default=0)
    name            = models.CharField(default='New Budget', max_length=100, null=False)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)
    category        = models.ForeignKey('Category', null=True)



class Goal(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    start_date      = models.DateField(blank=False)
    end_date        = models.DateField(blank=True, default='')
    amount          = models.IntegerField(default=0)
    name            = models.CharField(default='New Goal', max_length=100, null=False)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)


class Category(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)
    name            = models.CharField(default='Category', max_length=100, null=False)