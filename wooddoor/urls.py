"""
URL configuration for wooddoor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    StaticViewSitemap, ProductSitemap, ServiceSitemap,
    PortfolioSitemap, ShopProductSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'services': ServiceSitemap,
    'portfolio': PortfolioSitemap,
    'shop': ShopProductSitemap,
}

def google_verification(request):
    return HttpResponse(
        "google-site-verification: google555cb4c5a021e97e.html",
        content_type="text/html"
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path(
        "google555cb4c5a021e97e.html",
        google_verification
    ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('products/', include('products.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('shop/', include('shop.urls')),
    path('about_us/', include('aboutus.urls')),
    path('search/', include('search.urls')),
    path('contact/', include('contact.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)