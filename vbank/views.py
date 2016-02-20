from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class OverviewView(TemplateView):

    template = 'overview.html'

    def dispatch(self, request):
        return render(request, self.template)