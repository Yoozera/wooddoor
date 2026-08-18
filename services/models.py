from django.db import models
from django.urls import reverse

from django.utils.text import slugify


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "دسته بندی خدمات"
        ordering = ['name']

class Service(models.Model):
    category = models.ManyToManyField(ServiceCategory,related_name='services')
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100,
                                  blank=True,
                                  help_text="نام کلاس آیکون (مثال: fa fa-home برای FontAwesome یا flaticon-helmet-1 برای FlatIcon)")
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    extra_image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    extra_image2 = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    advantages = models.TextField(blank=True,help_text='مزایای این سرویس را بنویسید 2')
    our_approach = models.TextField(blank=True, help_text="توضیحات مربوط به رویکرد ما")
    work_proccess = models.TextField(blank=True, help_text="پروسه کاری")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'خدمات '


class ServiceStep(models.Model):
    service = models.ForeignKey(Service,related_name='steps',on_delete=models.CASCADE,verbose_name="سرویس مربوطه")
    title = models.CharField(max_length=100,verbose_name="عنوان تحقیق")
    text = models.TextField(verbose_name="متن توضیحات")
    image = models.ImageField(upload_to='services/steps/',blank=True,null=True,verbose_name="تصویر مرحله(اختیاری")
    order = models.PositiveIntegerField(default=0,verbose_name="ترتییب نمایش")

    class Meta:
        ordering = ['order']
        verbose_name = 'مرحله سرویس'
        verbose_name_plural = 'مراحل سرویس'

    def __str__(self):
        return f"{self.service.name} - {self.title} "











