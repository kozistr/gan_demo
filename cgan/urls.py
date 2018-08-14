from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^about/$', view=views.about, name='about'),
    url(r'^demo/$', view=views.gen_cgan_image, name='demo'),
]
