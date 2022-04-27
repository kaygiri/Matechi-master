from django.db import models
from SubCategories.models import SubCategory
from Shop.models import Product
from Brand.models import Brands

# Top Banner model
class Bannercarousel(models.Model):
    created_on = models.DateField(null = True, blank = True, auto_now_add = True)

    class Meta:
        verbose_name = 'Top Banner Carousel (Slideshow)'

class Banners(models.Model):
    bannercarousel = models.ForeignKey(Bannercarousel, on_delete = models.CASCADE)      
    image = models.ImageField(upload_to = 'images/Banner_Images')
    link = models.CharField(max_length = 350, blank = True, null = True)

# The product carousel models    

class Featured_Products(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name = 'Featured Products'

    def __str__(self):
        return self.name    

class SubCategory1(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory #1'

    def __str__(self):
        return self.subcategory.name 

class SubCategory2(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory #2'    

class SubCategory3(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory #3'          

class Showcase_Products1(models.Model):
    featured_products = models.ForeignKey(Featured_Products, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Feature Products'

class Showcase_Products2(models.Model):
    subcategory1 = models.ForeignKey(SubCategory1, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Feature Products'

class Showcase_Products3(models.Model):
    subcategory2 = models.ForeignKey(SubCategory2, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Feature Products'

class Showcase_Products4(models.Model):
    subcategory3 = models.ForeignKey(SubCategory3, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Feature Products'                        

class Feature_Brands(models.Model):
    class Meta:
        verbose_name = 'Shop By Brands'    

class Showcase_brand(models.Model):
    feature_brands = models.ForeignKey(Feature_Brands, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Feature Brands'

class Banner2Carousel(models.Model):
    class Meta:
        verbose_name = 'Banner Collection #2 (Slideshow)'

class BannerImages(models.Model):
    banner2carousel = models.ForeignKey(Banner2Carousel, on_delete = models.CASCADE)
    images = models.ImageField(upload_to = 'images/Banner_Images')
    link = models.CharField(max_length = 350, null = True, blank = True)




            

  


