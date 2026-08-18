from django.views.generic import TemplateView
from django.db.models import Q

from portfolio.models import Portfolio
from products.models import Product
from services.models import Service
from shop.models import ShopProduct


class SearchView(TemplateView):
    template_name = 'search/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()
        results = []

        if query:
            portfolios = Portfolio.objects.filter(
                Q(name__icontains=query) | Q(short_description__icontains=query) | Q(content__icontains=query),
                is_active=True,
            )
            products = Product.objects.filter(
                Q(name__icontains=query) | Q(short_description__icontains=query) | Q(description__icontains=query),
                is_available=True,
            )
            services = Service.objects.filter(
                Q(name__icontains=query) | Q(short_description__icontains=query) | Q(description__icontains=query),
                is_active=True,
            )
            shop_products = ShopProduct.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

            for p in portfolios:
                results.append(self._build_item(p, p.name, p.short_description, 'نمونه‌کار', query, p.get_absolute_url() if hasattr(p, 'get_absolute_url') else '#'))
            for p in products:
                results.append(self._build_item(p, p.name, p.short_description, 'محصول', query, p.get_absolute_url()))
            for s in services:
                results.append(self._build_item(s, s.name, s.short_description, 'خدمت', query, s.get_absolute_url()))
            for sp in shop_products:
                results.append(self._build_item(sp, sp.name, sp.description, 'فروشگاه', query, sp.get_absolute_url()))

            results.sort(key=lambda x: x['score'], reverse=True)

        context.update({
            'query': query,
            'results': results,
            'total_count': len(results),
        })
        return context

    def _build_item(self, obj, title, description, type_label, query, url):
        score = 2 if query.lower() in title.lower() else 1
        return {
            'object': obj,
            'title': title,
            'description': description,
            'type': type_label,
            'url': url,
            'image': getattr(obj, 'image', None),
            'score': score,
        }