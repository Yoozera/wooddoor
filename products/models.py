from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= "دسته بندی ها"
        ordering = ['name']

class WoodType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "جنس چوب"
        verbose_name_plural = "انواع چوب"
        ordering = ['name']


class Product(models.Model):
    service = models.ManyToManyField(
        'services.Service',
        related_name='products',
        blank=True,
        verbose_name='سرویس مرتبط',
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    wood_type = models.ForeignKey(WoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

