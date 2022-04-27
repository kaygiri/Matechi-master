from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category_image = models.ImageField(null=True,blank=True,upload_to='images/category images/')
    priority = models.IntegerField(unique=True)

    # For SEO
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 300, blank = True, null = True)
    page_title = models.CharField(max_length = 300)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)    

    class Meta:
        ordering = ('priority',)   
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 


class BannerImage(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(blank = True, null = True, upload_to = 'images/category banners/')
    link = models.CharField(max_length = 350, null = True, blank = True)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'    