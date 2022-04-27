from django.db import models
from Categories.models import Category
from django.utils.text import slugify

class Brands(models.Model):
    name = models.CharField(max_length = 200, unique = True , null = False)
    brand_logo = models.ImageField(upload_to='images/brand images', null = True, blank = True)
    super_category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, blank = True)
    slug = models.SlugField(unique = True, max_length = 200)
    brand_priority = models.IntegerField(unique = True)

    # For SEO
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 300, blank = True, null = True)
    page_title = models.CharField(max_length = 300)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brands, self).save(*args, **kwargs)


    class Meta:
        ordering = ('brand_priority',)
        verbose_name = 'Brands' 
        verbose_name_plural = 'Brands'    
