from django.shortcuts import render
from Brand.models import Brands

def brand_mall(request):
    brands = Brands.objects.all()
    context = {'brands' : brands}
    return render(request, 'brandmall.html', context)
