from django.contrib import admin
from .models import Category, BannerImage
from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

class BannerAdmin(admin.StackedInline):
    extra = 0
    model = BannerImage
    classes = ['tab-banner']

class CategoryAdmin(DjangoTabbedChangeformAdmin,admin.ModelAdmin):
    list_display = ('name','slug','category_image','priority')
    list_filter = ('name',)
    search_fields = ['name']
    list_per_page = 20
    inlines = [BannerAdmin]

    fieldsets = (
    (None, {
        'classes': ('tab-general',),
        'fields' : ('name','category_image','priority') 
    }),
    ('SEO',{
        'classes': ('tab-seo',),
        'fields' : ('meta_description', 'meta_keywords', 'page_title')
    }),
    )

    tabs = [
        ("General", ["tab-general"]),
        ("SEO", ["tab-seo"]),
        ('Banner', ['tab-banner'])
    ]
admin.site.register(Category,CategoryAdmin)
