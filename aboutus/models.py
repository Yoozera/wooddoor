from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="درباره ما")
    bold_text = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


class FunFact(models.Model):
    title = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.client_name

class SiteBackground(models.Model):
    testimonial_bg = models.ImageField(upload_to='backgrounds/',
                                         help_text="بک‌گراند بخش نظرات مشتریان")

    def __str__(self):
        return "تنظیمات بک‌گراند سایت"

    class Meta:
        verbose_name = "بک‌گراند سایت"
        verbose_name_plural = "بک‌گراندهای سایت"