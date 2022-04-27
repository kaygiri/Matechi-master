from django.contrib import admin
from .models import *

class BannersAdmin(admin.StackedInline):
    model = Banners
    extra = 0


class BannerCarouselAdmin(admin.ModelAdmin):
    inlines = [BannersAdmin]

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Bannercarousel,BannerCarouselAdmin)

# Register Showcase Products
class Showcase1_Admin(admin.StackedInline):
    model = Showcase_Products1
    extra = 0

class Showcase2_Admin(admin.StackedInline):
    model = Showcase_Products2
    extra = 0

class Showcase3_Admin(admin.StackedInline):
    model = Showcase_Products3
    extra = 0

class Showcase4_Admin(admin.StackedInline):
    model = Showcase_Products4
    extra = 0   

# Add main models with their respective inlines
class FeatureAdmin(admin.ModelAdmin): 
    inlines = [Showcase1_Admin] 

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True   

class SubCategory1Admin(admin.ModelAdmin):
    inlines = [Showcase2_Admin] 

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True    

class SubCategory2Admin(admin.ModelAdmin):
    inlines = [Showcase3_Admin]

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True  

class SubCategory3Admin(admin.ModelAdmin):
    inlines = [Showcase4_Admin]

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True

# Add featured brands
class ShowcaseBrandsAdmin(admin.StackedInline):
    model = Showcase_brand
    extra = 0

class FeatureBrandsAdmin(admin.ModelAdmin):    
    inlines = [ShowcaseBrandsAdmin]

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True

# Add banner 2
class Banner2Images(admin.StackedInline):
    model = BannerImages
    extra = 0


class Banner2Admin(admin.ModelAdmin):
    inlines = [Banner2Images]  

    def has_add_permission(self, request):
        return True
        
    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Featured_Products, FeatureAdmin)
admin.site.register(SubCategory1, SubCategory1Admin)
admin.site.register(SubCategory2, SubCategory2Admin)
admin.site.register(SubCategory3, SubCategory3Admin)  
admin.site.register(Feature_Brands, FeatureBrandsAdmin) 
admin.site.register(Banner2Carousel, Banner2Admin)


# Add showcase brands and their inlines
class ShowcaseBrandAdmin(admin.StackedInline):
    model = Showcase_brand
    extra = 0

class FeatureBrandAdmin(admin.ModelAdmin):
    inlines = [ShowcaseBrandAdmin] 


# Add Banner2Carousel
class BannerImagesAdmin(admin.StackedInline):
    model = BannerImages
    extra = 0

class Banner2Carousel(admin.ModelAdmin):
    inlines = [BannerImagesAdmin]           
