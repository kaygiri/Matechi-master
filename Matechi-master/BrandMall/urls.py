from django.urls import path
from BrandMall import views

urlpatterns = [
    path('the-nepal-mall-store/', views.brand_mall, name = 'brand-mall'),
]