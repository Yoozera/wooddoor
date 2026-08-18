from django.db import models
from django.utils.text import slugify
from django.urls import reverse







class PortFolioCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان دسته بندی')
    slug = models.SlugField(unique=True,blank=True,verbose_name='اسلاگ')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class PortfolioTag(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='نام تگ')
    slug = models.SlugField(unique=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_tag_list', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ '
        verbose_name_plural = 'تگ ها'

class Portfolio(models.Model):
    name = models.CharField(max_length=100,verbose_name='عنوان')
    slug = models.SlugField(unique=True,blank=True,verbose_name='اسلاگ')
    categories = models.ManyToManyField(PortFolioCategory,related_name='post',verbose_name='دسسته بندی های')
    tags = models.ManyToManyField(PortfolioTag,related_name='portfolio',blank=True,verbose_name='تگ ها')
    image = models.ImageField(upload_to='portfolio/images/',verbose_name='تصویر شاخص')
    short_description = models.TextField(max_length=500,blank=True,verbose_name='خلاصه متن')
    content = models.TextField(verbose_name='متن کامل')
    is_active = models.BooleanField(default=True,verbose_name='فعال بودن')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='آخرین ویرایش')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نمونه کار/پست'
        verbose_name_plural = 'نمونه کارها/پست ها'
        ordering = ['-created_at']

class InstagramGallery(models.Model):
    image = models.ImageField(upload_to='portfolio/instagram/',verbose_name='تصویر')

    def __str__(self):
        return f"instagram image {self.image}"

    class Meta:
        verbose_name = 'تصویر اینستاگرام'
        verbose_name_plural = 'تصویرهای اینستاگرام'
        ordering = ['-id']



















