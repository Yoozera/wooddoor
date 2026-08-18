# from .models import ShopCategory, ShopProduct
#
#
# def sidebar_data(request):
#     """
#     این تابع داده‌های مورد نیاز سایدبار را در تمام صفحات وب‌سایت
#     به صورت خودکار در دسترس قرار می‌دهد.
#     """
#     return {
#         'sidebar_categories': ShopCategory.objects.all(),
#         'sidebar_popular_products': ShopProduct.objects.filter(is_popular=True)[:3],
#     }