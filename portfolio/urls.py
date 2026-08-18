from django.urls import path
from .views import PortfolioListView, PortfolioDetailView, PortfolioTagListView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('tag/<slug:slug>/', PortfolioTagListView.as_view(), name='portfolio_tag_list'),
]