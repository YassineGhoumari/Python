from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^surveys/$', views.surveys),
    url(r'^process$', views.process_form),
    url(r'^result$', views.display_result),
]
