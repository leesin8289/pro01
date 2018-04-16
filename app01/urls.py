from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^show_static$', views.show_static),
    url(r'^add_user$', views.add_user),
    url(r'^show_page$', views.show_page),
    url(r'^show_page/(\d+)$', views.show_page),
    url(r'^show_areas$', views.show_areas),
    url(r'^get_children/(\d+)$', views.get_children),
]
