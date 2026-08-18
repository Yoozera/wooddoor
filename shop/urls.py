from django.urls import path
from .views import ShopProductListView, ShopProductDetailView, CategoryProductListView,ShopTagListView

app_name = 'shop'

urlpatterns = [
    path('', ShopProductListView.as_view(), name='shop_list'),
    path('<slug:slug>/', ShopProductDetailView.as_view(), name='shop_detail'),
    path('category/<slug:slug>/', CategoryProductListView.as_view(), name='category_list'),
    path('tag/<slug:slug>/', ShopTagListView.as_view(), name='tag_list'),
]