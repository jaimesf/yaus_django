# -*- encoding: utf-8 -*-
from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.index, name='creator'),
    url(r'^(?P<id>.*)[/]?$', views.redirectioner, name='redirectioner'),

]
