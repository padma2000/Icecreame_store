from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('about', views.about, name='about us'),
    path('services', views.Services, name='services'),
    path('contact', views.contact, name='contact'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('tracker', views.tracker, name='')
    
]