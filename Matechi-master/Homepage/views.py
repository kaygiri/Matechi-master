from django.shortcuts import render,get_object_or_404
from Shop.models import Product,PostImages
from Brand.models import Brands
from Categories.models import Category
from SubCategories.models import SubCategory
from django.http import HttpResponseNotFound,HttpResponseRedirect
from ast import literal_eval
import json
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from functools import reduce
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Commerce.models import Cart
from .models import *
from datetime import date

def default_query_params(cat_dict,slug):
    default_cat_list = []
    for c in cat_dict:
        default_cat_list.append(c)

    price_range = Product.objects.filter(Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug)).values_list('current_price',flat=True)
    default_price_json = json.loads(price_range_finder(price_range))   

        
    print(default_cat_list, default_price_json['max_price'], 'default')
    return default_cat_list, default_price_json

def price_range_finder(price_range):
    price_json = {}
    max_price = 0
    min_price = 0
    for price in price_range:
        # max price find first
        if price > max_price:
            max_price = price

        # min price find now
        if min_price == 0:
            min_price = price 
        else:
            if price < min_price:
                min_price = price        

    price_json['max_price'] = max_price
    price_json['min_price'] = min_price
    if max_price == min_price:
        price_json['min_price'] = 0
    price_json = json.dumps(price_json)                      
    return price_json



def resolve_sort_param(sort_param):
    if sort_param[0] == 'default sorting':
        return 'product_name'
    elif sort_param[0] == 'price high to low':
        return '-current_price'
    elif sort_param[0] == 'price low to high':
        return 'current_price'
    elif sort_param[0] == 'date':
        return 'published_date'
    elif sort_param[0] == 'rating':
        return '-int_average_rating'
    else:
        return 'product_name'        
                    


# Returns a dictionary with the category and it's number of the avalable products
def process_category_sidebar(slug):
    sub_cat = Product.objects.filter(Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug))
    
    category_dict = {}
    for sc in sub_cat:
        #print('this is sc', sc.subcategory)
        sc_list = sc.subcategory
    #for s in sub:
        #ss = eval(s)
        #print(ss, 'this is ss')

        if sc_list != None:
            if sc_list not in category_dict:
                category_dict.update({sc_list:1})
            else:
                category_dict[sc_list] = category_dict[sc_list] + 1    
        #print(category_dict)  `
    return category_dict  

def search(request,slug):
    option_list = []
    # The default view will be in order of Alphabetically
    page_num = 1

    total_count = Product.objects.filter(Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug)).count()
    value = Product.objects.filter(Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug)).order_by('product_name')
    images = PostImages.objects.all()
    brand_value = Brands.objects.filter(name__iexact = slug)

    cat_dict = process_category_sidebar(slug)

    paginator = Paginator(value, 16) 
    value = paginator.page(page_num) 

    default_cat_list,default_price_json = default_query_params(cat_dict,slug)


    # Process the filters 
    if request.method == 'GET':
        if request.is_ajax():
            text = request.GET.get('text')
            #print(text)
            if text == 'price-range':
                price_range = Product.objects.filter(Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug)).values_list('current_price',flat=True)
                price_range_json = price_range_finder(price_range)
                #print(price_range_json)

                return HttpResponse(price_range_json,content_type = 'application/json')


        if len(request.GET)!= 0:
            #print('At Least one query string ...')

            # Pagination
            page_num = request.GET.get('page', 2)

            category_param = request.GET.getlist('category',default_cat_list)
            sort_param = request.GET.getlist('sort_by',['default sorting'])
            sort_parameter = resolve_sort_param(sort_param)
            max_price_param = request.GET.get('max_price')
            if max_price_param == None:
                max_price_param = default_price_json['max_price']
            else:    
                max_price_param = max_price_param.strip('NPR ')    
            min_price_param = request.GET.get('min_price')
            if min_price_param == None:
                min_price_param = default_price_json['min_price']
            else:    
                min_price_param = min_price_param.strip('NPR ')

            # Turn list of values into one big Q objects  
            query = reduce(lambda q,category_param: q|Q(subcategory__icontains = category_param),category_param, Q())  

            value = Product.objects.filter(query,Q(product_name__icontains = slug)|Q(brand__icontains = slug)|Q(category__icontains = slug)|Q(subcategory__icontains = slug),current_price__range =(min_price_param,max_price_param)).order_by(sort_parameter)
  
            print(value)       

            paginator = Paginator(value, 16)
            try:
                value = paginator.page(page_num)
            except PageNotAnInteger:
                value = paginator.page(page_num)
            except EmptyPage:
                value = paginator.page(paginator.num_pages) 
                    

        context = {'value' : value, 'brand_value' : brand_value, 'category_dict' : cat_dict, 'count' : total_count, 'brand_name' : slug}
        return render(request,'search.html',context) 

    context = {'value':value,'brand_value':brand_value, 'category_dict' : cat_dict, 'count' : total_count, 'brand_name' : slug}        
    return render(request, 'search.html', context)        


def home(request):
    # Get the top banners
    banner1 = Bannercarousel.objects.all()

    # Get 5 random SubCategory
    subcategory = SubCategory.objects.all().order_by('?')[:5]

    # Get the featured products
    featured_products = Featured_Products.objects.all()

    # Get Subcategory #1
    subcategory1 = SubCategory1.objects.all()
    if subcategory1:
        subcat1 = str((subcategory1[0].subcategory))

        products1 = Product.objects.filter(subcategory__iexact = subcat1).order_by('?')[:10]

    else:
        subcat1 = ''
        products1 = ''    

    # Get Subcategory #2
    subcategory2 = SubCategory2.objects.all()
    if subcategory2:
        subcat2 = str((subcategory2[0].subcategory))

        products2 = Product.objects.filter(subcategory__iexact = subcat2).order_by('?')[:10]

    else:
        subcat2 = ''
        products2 = ''     

    # Get Subcategory #3
    subcategory3 = SubCategory3.objects.all()
    if subcategory3:
        subcat3 = str((subcategory3[0].subcategory))

        products3 = Product.objects.filter(subcategory__iexact = subcat3).order_by('?')[:10]

    else:
        subcat3 = ''
        products3 = ''    

    # Get featured brands
    feature_brands = Feature_Brands.objects.all()

    
    # Get Banner 2
    banner2 = Banner2Carousel.objects.all()

    # SEO for homepage
    todays_date = date.today()

    context = {'banner1' : banner1, 'subcategory' : subcategory, 'featured_products' : featured_products, 'subcat1' : subcat1, 'products1' : products1, 'subcat2' : subcat2, 'products2' : products2, 'subcat3' : subcat3, 'products3' : products3, 'fb' : feature_brands, 'banner2' :banner2, 'current_year' : todays_date.year}
    return render(request, 'index.html', context)



def contact(request):
    return render(request, 'contact.html')




