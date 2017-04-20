from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bom/(?P<id>\d+)/$', views.bom_detail, name='bom_detail'),
]