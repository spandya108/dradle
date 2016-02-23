from django.db import models
import uuid


class Transaction(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount          = models.FloatField(default=0)
    date            = models.DateTimeField(default=None, blank=True)
    month           = models.DateTimeField(default=None, blank=True)
    type            = models.CharField(default='', blank=True, max_length=100)
    institution     = models.CharField(default='', blank=True, max_length=100)
    label           = models.CharField(max_length=100)
    description     = models.TextField(null=True)

    def __str__(self):
        return str(self.institution) + ': ' + str(self.label) + ' - ' + str(self.amount)

    @property
    def name(self):
        return self.label.title()
