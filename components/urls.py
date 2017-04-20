from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.components, name='components'),
    url(r'^(?P<id>\d+)$', views.components_detail, name='components_detail'),
]