from django.contrib import admin
from django import forms
from .models import Brands
from Categories.models import Category
from SubCategories.models import SubCategory
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

"""
def getcategorychoices():
    return [
        (cat.name, cat.name) for cat in Category.objects.all()
    ]

def getsubcategorychoices():
    return [
        (subcat.name, subcat.name) for subcat in SubCategory.objects.all()
    ]    
"""

"""
class BrandAdminForm(forms.ModelForm):
    #super_category = forms.ModelChoiceField(queryset = Category.objects.all(), widget = forms.Select, required = True)
    super_category = forms.ChoiceField(choices = getcategorychoices, required = False)
"""

class BrandAdmin(DjangoTabbedChangeformAdmin, admin.ModelAdmin):
    list_display = ('name','brand_logo','super_category','brand_priority')  
    list_filter = ('name',)  
    search_fields = ['name']
    list_per_page = 20

    fieldsets = (
    (None, {
        'classes': ('tab-general',),
        'fields' : ('name','brand_logo','super_category','brand_priority') 
    }),
    ('SEO',{
        'classes': ('tab-seo',),
        'fields' : ('meta_description', 'meta_keywords', 'page_title')
    }),
    )

    tabs = [
        ("General", ["tab-general"]),
        ("SEO", ["tab-seo"]),
    ]


admin.site.register(Brands,BrandAdmin)    

