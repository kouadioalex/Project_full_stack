
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import  static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='homes'),
    path('article/',include('Articles.urls') ),
    path('contact/', views.contact_view, name='contacts' ),
    path('remercis/', views.remerciment_view, name='remercis' )
    
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
