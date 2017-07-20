from django.conf.urls import url

from operationalSearch import views

urlpatterns = [
    url(r'^$', views.operationalSearch, name='operationalSearch'),
]
