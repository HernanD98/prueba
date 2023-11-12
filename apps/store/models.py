from django.db import models
from django.urls import reverse
from apps.category.models import Category

# Create your models here.

class Marca(models.Model):
    marca_name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    marca_web = models.URLField(max_length=500, unique=True)
    
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
    
    def __str__(self):
        return self.marca_name
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name
    

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    def tallas(self):
        return super(VariationManager, self).filter(variation_category='talla', is_active=True)

    
variation_category_choices = (
    ('color', 'color'),
    ('talla', 'talla'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_category + ':' + self.variation_value