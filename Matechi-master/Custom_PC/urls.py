from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from Custom_PC import views

 
urlpatterns = [
    path('custom-pc-nepal/', views.custom_pc, name = 'custom-pc'),
    path('custom-pc-nepal/checkout/', views.custom_pc_checkout, name = 'custom-pc-checkout')
] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)