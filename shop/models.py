from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class ShopCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='دسته بندی ها')
    slug = models.SlugField(unique=True, blank=True, verbose_name='اسلاگ')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

class ShopTag(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='نام تگ')
    slug = models.SlugField(unique=True,blank=True,verbose_name='اسلاگ')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('shop:tag_list', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class ShopProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    slug = models.SlugField(unique=True, blank=True, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='shopproduct/', verbose_name='تصویر')
    category = models.ManyToManyField(ShopCategory, related_name='shop_products', verbose_name='دسته‌بندی')
    is_popular = models.BooleanField(default=False, verbose_name='محصول محبوب')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    rating = models.FloatField(default=0.0, verbose_name='امتیاز')
    review_count = models.IntegerField(default=0, verbose_name='تعداد نظرات')
    tags = models.ManyToManyField(ShopTag, related_name='products', blank=True, verbose_name='تگ ها')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:shop_detail', kwargs={'slug': self.slug})


class ShopProductImage(models.Model):
    shop_product = models.ForeignKey(ShopProduct, related_name='extra_image', on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='shopproduct/gallery', verbose_name='تصاویر')

    def __str__(self):
        return f"{self.shop_product.name} - image {self.id}"

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصول'

