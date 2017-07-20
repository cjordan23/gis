from django.conf.urls import url

from operationalTrack import views

urlpatterns = [
    url(r'^$', views.operationalTrack, name='operationalTrack'),
]
