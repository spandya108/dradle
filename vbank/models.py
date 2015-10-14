from django.db import models
import uuid

# Create your models here.


class Transaction(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    credit          = models.IntegerField(default=0)
    debit           = models.IntegerField(default=0)
    combined        = models.BooleanField(default=False)
    date            = models.DateTimeField(default=None, blank=True)
    month           = models.DateTimeField(default=None, blank=True)
    type            = models.CharField(default='', blank=True, max_length=100)
    institution     = models.CharField(default='', blank=True, max_length=100)
    budgets         = models.ManyToManyField('Budget', blank=True)
    goals           = models.ManyToManyField('Goal', blank=True)
    categories      = models.ManyToManyField('Category', blank=True)
    label           = models.CharField(max_length=100)
    description     = models.TextField(null=True)
    user            = models.ForeignKey('User', null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '[-' + str(self.credit) + '][+' + str(self.debit) + ']'

    def save(self, *args, **kwargs):

        self.user.update_balance(self.credit, self.debit)
        super(Transaction, self).save(*args, **kwargs)

    @property
    def name(self):
        return self.label.title()


class PhysicalTransaction(Transaction):

    v_transaction   = models.ForeignKey('VirtualTransaction', null=True, blank=True)


class VirtualTransaction(Transaction):

    name            = models.CharField(null=False, max_length=100, default='')
    count           = models.IntegerField(default=1)


class Budget(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount          = models.IntegerField(default=0)
    remaining       = models.IntegerField(default=0)
    label           = models.CharField(default='New Budget', max_length=100, null=False)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)
    category        = models.ForeignKey('Category', null=True)

    def __str__(self):
        return self.name + ': ' + str(self.amount) + ' (' + str(self.remaining) + ')'

    @property
    def name(self):
        return self.label.title()


class Goal(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    start_date      = models.DateField(blank=False)
    end_date        = models.DateField(blank=True, default='')
    amount          = models.IntegerField(default=0)
    label           = models.CharField(default='New Goal', max_length=100, null=False)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)

    def __str__(self):
        return self.name + ': ' + self.amount

    @property
    def name(self):
        return self.label.title()


class Category(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    p_transactions  = models.ManyToManyField('PhysicalTransaction', blank=True)
    v_transactions  = models.ManyToManyField('VirtualTransaction', blank=True)
    label           = models.CharField(default='Category', max_length=100, null=False)
    parent          = models.ForeignKey('Category', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.label.title()


class User(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    safe_to_spend   = models.FloatField(default=0.0, null=False, blank=False)
    balance         = models.FloatField(default=0.0, null=False, blank=False)
    first_name      = models.CharField(null=False, max_length=100)
    last_name       = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def update_balance(self, credit, debit):
        self.balance = self.balance - credit + debit

    def reset_balance(self):
        self.balance = 0.0