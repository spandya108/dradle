from django.conf.urls import url

from views import OverviewView

urlpatterns = [
    url(r'^$', OverviewView.as_view(), name='overview')
]