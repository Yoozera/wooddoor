from django.contrib import admin
from .models import Category,Product,WoodType

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',"slug")
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(WoodType)
class WoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name',"slug")
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_service',
        'category',
        'wood_type',
        'is_available',
        'created_at',
    )
    def get_service(self, obj):
        return ", ".join([service.name for service in obj.service.all()])
    get_service.short_description = 'سرویس های مرتبط'

    list_filter = ('is_available','category','wood_type')

    search_fields = ('name','short_description')

    list_editable = ('is_available',)

    prepopulated_fields = {'slug': ('name',)}















