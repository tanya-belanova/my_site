from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_words', views.add_words),
    path('learn_words', views.learn_words),
    path('statistics', views.statistics)
]
