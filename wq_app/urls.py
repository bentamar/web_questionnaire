from django.conf.urls import url

from . import views

app_name = 'wq_app'
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^index/$', views.index),
    url(r'^activate/(?P<key>.+)$', views.activation),
    url(r'^new-activation-link/(?P<user_id>\d+)/$', views.new_activation_link),
]
