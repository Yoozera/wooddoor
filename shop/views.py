from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import ShopCategory, ShopProduct , ShopTag


class ShopProductListView(ListView):
    model = ShopProduct
    template_name = 'shop/shop.html'
    context_object_name = 'shop_products'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('category')

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        order_by = self.request.GET.get('order')
        if order_by == 'newest':
            queryset = queryset.order_by('-created_at')
        elif order_by == 'popular':
            queryset = queryset.order_by('-is_popular', '-created_at')
        elif order_by == 'alphabetical':
            queryset = queryset.order_by('name')
        else:
            queryset = queryset.order_by('is_popular', '-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        context['total_products'] = ShopProduct.objects.count()
        context['search_query'] = self.request.GET.get('q')
        context['popular_products'] = ShopProduct.objects.filter(is_popular=True).order_by('-created_at')[:4]
        context['all_tags'] = ShopTag.objects.all()
        return context


class ShopProductDetailView(DetailView):
    model = ShopProduct
    template_name = 'shop/shop-single.html'
    context_object_name = 'shop_product'
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_product = self.get_object()

        similar_products = ShopProduct.objects.filter(
            category__in=shop_product.category.all()
        ).exclude(id=shop_product.id).distinct()[:4]

        context['similar_products'] = similar_products
        context['total_products'] = ShopProduct.objects.count()
        context['categories'] = ShopCategory.objects.all()
        context['popular_products'] = ShopProduct.objects.filter(is_popular=True).order_by('-created_at')[:5]
        context['search_query'] = self.request.GET.get('q')
        context['all_tags'] = ShopTag.objects.all()

        return context


class CategoryProductListView(ListView):
    model = ShopProduct
    template_name = 'shop/shop.html'
    context_object_name = 'shop_products'
    paginate_by = 9

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        self.category = get_object_or_404(ShopCategory, slug=category_slug)
        queryset = ShopProduct.objects.filter(category=self.category).prefetch_related('category').distinct()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        order_by = self.request.GET.get('order')
        if order_by == 'newest':
            queryset = queryset.order_by('-created_at')
        elif order_by == 'popular':
            queryset = queryset.order_by('-is_popular', '-created_at')
        elif order_by == 'alphabetical':
            queryset = queryset.order_by('name')
        else:
            queryset = queryset.order_by('is_popular', '-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        context['total_products'] = ShopProduct.objects.count()
        context['current_category'] = self.category
        context['search_query'] = self.request.GET.get('q')
        context['all_tags'] = ShopTag.objects.all()
        return context

class ShopTagListView(ListView):
    model = ShopProduct
    template_name = 'shop/shop.html'
    context_object_name = 'shop_products'
    paginate_by = 9

    def get_queryset(self):
        self.tag = get_object_or_404(ShopTag, slug=self.kwargs['slug'])
        return ShopProduct.objects.filter(tags=self.tag).prefetch_related('category').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ShopCategory.objects.all()
        context['total_products'] = ShopProduct.objects.count()
        context['current_tag'] = self.tag
        context['all_tags'] = ShopTag.objects.all()
        return context