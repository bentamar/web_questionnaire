from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', 'register'),
    url(r'^activate/(?P<key>.+)$', 'activation'),
    url(r'^new-activation-link/(?P<user_id>\d+)/$', 'new_activation_link'),
]
