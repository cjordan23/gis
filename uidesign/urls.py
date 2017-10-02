from django.conf.urls import url

from uidesign import views

urlpatterns = [
    url(r'^$', views.uidesign, name='uidesign'),
]
