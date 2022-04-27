from django.contrib import admin
from .models import *
from django import forms
from Brand.models import Brands
from Categories.models import Category
from SubCategories.models import SubCategory
from django.utils.html import format_html
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

# Function to get brand choices and type conversion to a tuple
def getBrandChoices():
    return [
        (brand.name, brand.name) for brand in Brands.objects.all()
    ]

# Function to get category choices and type conversion to a tuple
def getcategorychoices():
    return [
        (cat.name, cat.name) for cat in Category.objects.all()
    ]

def getsubcategorychoices():
    return [
        (subcat.name, subcat.name) for subcat in SubCategory.objects.all()
    ]    

class PostImagesAdmin(admin.StackedInline):
    model = PostImages
    extra = 0
    classes = ['tab-images']

class ReviewsAdmin(admin.StackedInline):
    model = Reviews
    extra = 0    
    classes = ['tab-reviews']
    list_per_page = 1


class ProductFormAdmin(forms.ModelForm):
    brand = forms.ChoiceField(choices = getBrandChoices, required = False)
    category = forms.ChoiceField(choices = getcategorychoices, required = False)
    subcategory = forms.ChoiceField(choices = getsubcategorychoices, required = False)

class ProductAdmin(DjangoTabbedChangeformAdmin, admin.ModelAdmin):
    # Save main model before related model
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            super().save_model(request, obj, form, change)
        else:
            pass 

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
        super().save_model(request, form.instance, form, change)

    list_display=('product_name','image_tag','published_date','availability','sale','new','current_price','brand','category','subcategory','quantity')
    list_filter = ('availability','sale','new','brand','category','subcategory')
    search_fields = ['product_name','brand','category']
    list_per_page = 20
    #prepopulated_fields = {'slug':('product_id',)}

    inlines = [PostImagesAdmin, ReviewsAdmin]
    form = ProductFormAdmin

    fieldsets = (
        (None, {
            'classes' : ('tab-general',),
            'fields' : ('product_name','description','model_number', 'specifications','overview','shipping_and_returns','published_date','availability','sale','new','previous_price', 'current_price','discount_percentage','thumbnail','brand','category','subcategory','quantity')
        }),
        ('SEO', {
            'classes' : ('tab-seo',),
            'fields' : ('meta_description', 'meta_keywords', 'page_title')
        }),
    )

    tabs = [
        ("General", ["tab-general"]),
        ("Images", ["tab-images"]),
        ("SEO", ["tab-seo"]),
        ("Reviews", ["tab-reviews"]),
    ]

    class Meta:
        model = Product    

admin.site.register(Product,ProductAdmin)
   
