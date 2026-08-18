from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service-detail.html'
    context_object_name = 'service'
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('steps')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        current_service = self.get_object()
        related_services = Service.objects.filter(
            category__in=current_service.category.all(),
        ).exclude(id=current_service.id).distinct()
        context['related_services'] = related_services
        context['related_products'] = self.object.products.all()

        return context
