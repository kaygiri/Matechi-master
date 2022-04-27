from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from Homepage import views
 
urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/<slug>', views.search, name = 'search'),
    path('contact/', views.contact, name = 'contact'),
] 