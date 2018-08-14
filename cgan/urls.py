from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^about/$', view=None, name='about'),
    url(r'^demo/$', view=None ,name='demo'),
]
