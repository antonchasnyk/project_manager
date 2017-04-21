from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.components, name='components'),
    url(r'^(?P<id>\d+)$', views.components_detail, name='components_detail'),
    url(r'^resistors/$', views.resistors, name='resistors'),
    url(r'^resistors/(?P<id>\d+)$', views.resistor_detail, name='resistor_detail'),
    url(r'^capacitors/$', views.capacitors, name='capacitors'),
    url(r'^capacitors/(?P<id>\d+)$', views.capacitor_detail, name='capacitor_detail'),
    url(r'^transistors/$', views.transistors, name='transistors'),
    url(r'^transistors/(?P<id>\d+)$', views.transistor_detail, name='transistor_detail'),
]