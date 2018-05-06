from django.conf.urls import url
import requests
from . import views

urlpatterns = [
    url(r'^$/', views.home, name='home'),
]


