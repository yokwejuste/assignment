from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('polls/about', views.about, name='about'),
    path('polls/contact', views.contact, name='contact'),
    path('polls/single-page', views.single_page, name='single_page')
]

 