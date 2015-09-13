from django.db import models
import uuid

# Create your models here.


class Transaction(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit          = models.IntegerField(default=0)
    debit           = models.IntegerField(default=0)
    combined        = models.BooleanField(default=False)
    virtual         = models.BooleanField(default=False)
    virtual_txn     = models.ForeignKey('self', related_name='virtual_txn', null=True, blank=True)
    bank            = models.CharField(max_length=100)
    date            = models.DateTimeField(default=None, blank=True)
    month           = models.DateField(default=None, blank=True)
    type            = models.CharField(default='', blank=True, max_length=100)
    bank            = models.CharField(default='', blank=True, max_length=100)

    def __str__(self):
        return '[-' + credit + '][+' + debit + ']'

    def combine_transactions(self, transactions):
        # if(not transactions):
        #     return False
        # else:
        #     if(self.virtual == False):
        #         self.combined = True

        #         virtual_txn = Transaction(
        #             id = uuid.uuid4(),

        #         )
        pass
