from django.db import models
from Categories.models import Category
from django.utils.text import slugify

class SubCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    super_category = models.ForeignKey(Category, on_delete = models.CASCADE, null =True, blank = True)
    slug = models.SlugField(max_length=200, unique=True)
    sub_category_image = models.ImageField(null = True, blank = True, upload_to='images/sub category images/')
    subcategory_priority = models.IntegerField(unique=True)

    # For SEO
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 300, blank = True, null = True)
    page_title = models.CharField(max_length = 300)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('subcategory_priority',) 
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'   
