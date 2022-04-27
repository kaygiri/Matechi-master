from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from Commerce.models import Order
from Shop.models import Product
from itertools import chain

def recommended_list(product):
    brand = product[0].brand
    subcategory = product[0].subcategory
    category = product[0].category

    related_products = Product.objects.filter(subcategory = subcategory).exclude(id__in = product)[:4]
    rel_list = related_products
    print(rel_list)

    return rel_list       



def detail_view(request,slug):   
    detail_product = Product.objects.filter(slug = slug)

    if detail_product:
        for d in detail_product:
            images = PostImages.objects.filter(product=d)


        rel_list = recommended_list(detail_product)    
                    
        context = {'product' : detail_product, 'images' : images, 'rel_list' : rel_list}
        return render(request,'detailed_product.html',context)

    else:
        context = {}
        return render(request,'detailed_product.html',context)   
    

def review(request):
    if request.method == 'POST':
        verified = 0
        user = request.user

        review = json.loads(request.body)
        rating = float(review['rating'])
        full_name = review['full_name']
        _review = review['review']
        product_id = int(review['productid'])

        # Check if the user has ever bought the product to review or not
        for o in Order.objects.filter(user = user):
            for oi in o.orderitem_set.all():
                if (oi.product.id == product_id):
                    verified = 1

        if (verified == 1):
            # If the purchase is verified, check if the user has already submitted a review
            _product = Product.objects.get(id = product_id)
            review_prev = _product.reviews_set.filter(user = user)
            if review_prev:
                data = {'valid': 'no', 'message' : 'Cannot Submit Review. You have already reviewed this product.'}
                return JsonResponse(data, content_type = 'application/json')
            else:    
                product = Product.objects.get(id = product_id)
                product.reviews_set.create(user = user, full_name = full_name, review = _review, rating = rating)
                product.save()

                data = {'valid': 'yes', 'message' : 'Review Successful'}
                return JsonResponse(data, content_type = 'application/json')

        else:
            data = {'valid': 'no', 'message' : 'Cannot Submit Review. You Need to buy the product first to review'}
            return JsonResponse(data, content_type = 'application/json')


    

