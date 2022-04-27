from django.contrib import admin
from .models import SubCategory
from Categories.models import Category
from django import forms
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

"""
def get_category_choices ():
    return [
        (cat.name, cat.name) for cat in Category.objects.all()
    ]

class SubCategoryAdminForm(forms.ModelForm):
    super_category = forms.ChoiceField(choices = get_category_choices, required = False)

"""

class SubCategoryAdmin(DjangoTabbedChangeformAdmin, admin.ModelAdmin):
    list_display = ('name','super_category','sub_category_image','subcategory_priority')
    list_filter = ('name',)
    search_fields = ['name']
    list_per_page = 20

    fieldsets = (
        (
            None, {
                'classes' : ('tab-general',),
                'fields' : ('name','super_category','sub_category_image','subcategory_priority')
            }
        ),
        (
            'SEO', {
                'classes' : ('tab-seo',),
                'fields' : ('meta_keywords', 'meta_description', 'page_title')
            }
        ),
    )

    tabs = [
        ("General", ["tab-general"]),
        ("SEO", ["tab-seo"]),
    ]


admin.site.register(SubCategory,SubCategoryAdmin)
