from django.urls import path
from Brand import views

 
urlpatterns = [
    path('brand/<slug>/',views.brand_view,name='brand'),
] 