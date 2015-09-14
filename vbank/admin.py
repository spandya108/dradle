from django.contrib import admin
from .models import (
    PhysicalTransaction,
    VirtualTransaction,
    Budget,
    Goal,
    Category
)

# Register your models here.
admin.site.register(PhysicalTransaction)
admin.site.register(VirtualTransaction)
admin.site.register(Budget)
admin.site.register(Goal)
admin.site.register(Category)
