from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_words', views.add_words, name='add_words'),
    path('learn_words/', views.learn_words, name='learn_words'),
    path('statistics', views.statistics, name='statistics')
]
