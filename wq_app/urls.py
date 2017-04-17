from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^activate/(?P<key>.+)$', views.activation),
    url(r'^new-activation-link/(?P<user_id>\d+)/$', views.new_activation_link),
]
