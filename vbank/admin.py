from django.contrib import admin
from .models import Transaction, VirtualTransaction

# Register your models here.
admin.site.register(Transaction)
admin.site.register(VirtualTransaction)
