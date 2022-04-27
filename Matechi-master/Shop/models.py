from django.db import models
import uuid
from datetime import date, datetime, timedelta
from django.template.defaultfilters import slugify
from django.template.defaultfilters import truncatechars 
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

availability_choices = (('YES','yes'),('NO','no'))

class Product(models.Model):
    product_name = models.CharField(max_length = 400)
    slug = models.SlugField(max_length = 200, unique = True, blank =True,default = '')
    description = models.TextField(blank = True, null = True)
    model_number = models.CharField(max_length = 200, null = True, blank = True)
    specifications = RichTextField(blank = True, null = True)
    overview = RichTextField(blank = True, null = True)
    shipping_and_returns = RichTextField(blank = True, null = True)
    published_date = models.DateField(default = date.today)
    availability = models.CharField(choices = availability_choices, max_length = 200)
    sale = models.CharField(max_length = 50, choices = availability_choices)
    new = models.CharField(max_length = 50, choices = availability_choices)
    previous_price = models.PositiveBigIntegerField(blank = True, null = True)
    current_price = models.PositiveBigIntegerField()
    discount_percentage = models.IntegerField(blank = True , null =True)
    thumbnail = models.ImageField(upload_to = 'images/product images')
    brand = models.CharField(max_length = 200, blank = True, null = True)
    category = models.CharField(max_length = 200, blank = True, null = True)
    subcategory = models.CharField(max_length = 200, blank =True, null = True)
    quantity = models.IntegerField(blank = True, null = True)

    total_review = models.IntegerField(blank = True, null = True, verbose_name = 'Total Reviews')
    average_rating = models.FloatField(blank = True, null = True, verbose_name = 'Average Rating')
    int_average_rating = models.IntegerField(blank = True, null = True)

    # For SEO
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 300, blank = True, null = True)
    page_title = models.CharField(max_length = 300)

    @property
    def short_description(self):
        return truncatechars(self.description,100)

    def image_tag(self):
        return mark_safe('<img src="%s" width="75" height="75" />' % (self.thumbnail.url))

    image_tag.short_description = 'Image' 

    def save(self, *args, **kwargs):
        # Save slug
        self.slug = slugify(self.product_name + '-' + 'price-nepal')

        # Override new
        today = date.today()    
        n_days_ago = today - timedelta(days=20)
        if self.published_date < n_days_ago:
            self.new = 'NO'
        else:
            self.new = 'YES'

        # Save discount percentage
        if self.previous_price:
            self.discount_percentage = (self.previous_price - self.current_price)/(self.previous_price) * 100      

        # Override rating
        count = 0
        rating = 0
        for e in self.reviews_set.all():   
            rating = rating + e.rating
            count = count + 1
        if count != 0:    
            self.average_rating = (rating / count)
            self.total_review = count   
        else:
            self.average_rating = 0
            self.total_review = 0

        # Change availability if quantity 0
        if self.quantity == 0:
            self.availability = 'NO'
        else:
            self.availability = 'YES'    

        # Save rating as in integer 
        self.int_average_rating = int(self.average_rating)


        # This line below save every fields of the model instance
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class PostImages(models.Model):
    product = models.ForeignKey(Product, default = None, on_delete = models.CASCADE)    
    images = models.ImageField(upload_to = 'images/product_images')  

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'    

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(User, on_delete = models.PROTECT, blank = True, null = True)
    created_on = models.DateTimeField(blank = True, null = True, auto_now_add = True)
    full_name = models.CharField(max_length = 200, verbose_name = 'Full name')
    review = models.TextField(blank = True, null = True)
    rating = models.FloatField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews' 

   




