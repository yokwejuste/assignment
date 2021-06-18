from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), 
    path('/about', views.about, name='about'),
    path('/news', views.news, name='news')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 
