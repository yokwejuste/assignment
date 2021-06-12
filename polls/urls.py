from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('polls/about', views.about, name='about'),
    path('polls/news', views.news, name='news')
]

 