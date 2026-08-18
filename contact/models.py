from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    phone = models.CharField(max_length=15, verbose_name='شماره تماس')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'

    def __str__(self):
        return f"{self.name} - {self.phone}"