
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.article_view, name='articles'),
    path('creer/', views.creer_view, name="creer" ),
    path('<slug:detail>/', views.detail_view, name="detail" ) 
    
]
