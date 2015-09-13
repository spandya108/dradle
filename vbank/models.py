from django.db import models
from uuid import uuid4

# Create your models here.


class Transaction(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    credit          = models.IntegerField(default=0)
    debit           = models.IntegerField(default=0)
    combined        = models.BooleanField(default=False)
    bank            = models.CharField(max_length=100)
    date            = models.DateTimeField(default=None, blank=True)
    month           = models.DateField(default=None, blank=True)
    type            = models.CharField(default='', blank=True, max_length=100)
    bank            = models.CharField(default='', blank=True, max_length=100)
