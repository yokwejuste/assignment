from django.urls import path

from . import views

urlpatterns = [
    path('polls/', views.index, name='index'), 
    path('polls/about', views.about, name='about')
]

 