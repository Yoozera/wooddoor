from django.contrib import admin
from .models import ShopCategory, ShopProduct, ShopTag, ShopProductImage


class ShopProductImageInline(admin.TabularInline):
    model = ShopProductImage
    extra = 1
    can_delete = True


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_category', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    inlines = [ShopProductImageInline]

    def display_category(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    display_category.short_description = 'دسته بندی ها'


@admin.register(ShopTag)
class ShopTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']