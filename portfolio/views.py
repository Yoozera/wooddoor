from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Portfolio, PortFolioCategory, PortfolioTag, InstagramGallery


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/blog.html'
    context_object_name = 'portfolios'
    paginate_by = 10

    def get_queryset(self):
        queryset = Portfolio.objects.filter(is_active=True).order_by('-created_at')
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(categories__id=category_id)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(short_description__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category')
        return context


class PortfolioTagListView(ListView):
    model = Portfolio
    template_name = 'portfolio/blog.html'
    context_object_name = 'portfolios'
    paginate_by = 10

    def get_queryset(self):
        self.tag = get_object_or_404(PortfolioTag, slug=self.kwargs['slug'])
        return Portfolio.objects.filter(is_active=True, tags=self.tag).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = self.tag
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/blog_details.html'
    context_object_name = 'portfolio'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Portfolio.objects.filter(is_active=True)