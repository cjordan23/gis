from django.conf.urls import url

from assetmgmt import views

urlpatterns = [
    url(r'^$', views.assetmgmt, name='assetmgmt'),
]
