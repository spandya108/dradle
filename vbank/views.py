from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import (
    Transaction
)

# Create your views here.

class OverviewView(TemplateView):

    template = 'overview.html'

    def dispatch(self, request):
        return render(
            request,
            self.template,
            {
                'transactions': Transaction.objects.all().order_by('-date'),
                'total': sum(Transaction.objects.all().values_list('amount', flat=True))
            })