from django.db import models

class SliderItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    subtitle = models.TextField(blank=True, verbose_name='توضیح کوتاه')
    image = models.ImageField(upload_to='core/slider/', verbose_name='تصویر')
    button_text = models.CharField(max_length=50,blank=True, default='آشنایی بیشتر', verbose_name='متن دکمه')
    button_link = models.URLField(blank=True, verbose_name='لینک دکمه')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن')

    class Meta:
        ordering = ['order']
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.title




class ProcessStep(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.TextField(verbose_name='توضیحات')
    icon_class = models.CharField(max_length=100, help_text="مثال: flaticon-light-bulb", verbose_name='کلاس آیکون')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    class Meta:
        ordering = ['order']
        verbose_name = 'مرحله کاری'
        verbose_name_plural = 'مراحل کاری'

    def __str__(self):
        return self.title
