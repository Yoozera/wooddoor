from django.contrib.sitemaps import Sitemap

from products.models import Product
from services.models import Service
from portfolio.models import Portfolio
from shop.models import ShopProduct
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = "https"
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        # اسم‌های URL رو با urls.py خودت چک کن
        return ['core:home', 'products:product_list', 'services:service_list',
                'portfolio:portfolio_list', 'shop:shop_list']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.filter(is_available=True)

    def lastmod(self, obj):
        return obj.updated_at


class ServiceSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class PortfolioSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Portfolio.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ShopProductSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ShopProduct.objects.all()

    def lastmod(self, obj):
        return obj.created_at