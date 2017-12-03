from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^register$', views.new_register),
    url(r'^login$', views.new_login),
	url(r'^quotes$', views.quotes),
]
