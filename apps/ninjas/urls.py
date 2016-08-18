from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.noninjas),
    url(r'^ninjas$', views.noninjas),
    url(r'^ninjas/(?P<color>[a-z]*)$', views.showaninja)
]
