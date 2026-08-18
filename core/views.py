from django.shortcuts import render
from django.views.generic import TemplateView

from .models import SliderItem, ProcessStep
from services.models import Service
from products.models import Product, Category as ProductCategory
from aboutus.models import FunFact, TeamMember, Testimonial
from portfolio.models import Portfolio
from shop.models import ShopProduct


class HomeView(TemplateView):
    template_name = "core/core.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # اسلایدر اصلی
        context['sliders'] = SliderItem.objects.filter(is_active=True)

        # محصولات محبوب فروشگاه (Welcome Section - ۶ تا، ۲ ردیف ۳ تایی)
        context['popular_products'] = ShopProduct.objects.filter(is_popular=True)[:6]

        # سرویس‌ها (FullWidth Section - با آیکون)
        context['services'] = Service.objects.filter(is_active=True)

        # آمار و ارقام (مشترک با about us)
        context['fun_facts'] = FunFact.objects.all()

        # دسته‌بندی محصولات + محصولات هر دسته (برای تب‌های پروژه)
        context['product_categories'] = ProductCategory.objects.prefetch_related('products').all()
        context['all_products'] = Product.objects.filter(is_available=True)

        # مراحل کاری
        context['process_steps'] = ProcessStep.objects.all()

        # تیم (مشترک)
        context['team_members'] = TeamMember.objects.all()

        # نظرات مشتریان (مشترک)
        context['testimonials'] = Testimonial.objects.all()

        # اخبار
        context['news_list'] = Portfolio.objects.filter(is_active=True)[:6]

        return context