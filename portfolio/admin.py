from django.contrib import admin
from .models import PortFolioCategory, PortfolioTag, Portfolio, InstagramGallery


@admin.register(PortFolioCategory)
class PortFolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)


@admin.register(PortfolioTag)
class PortfolioTagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name','get_categories','is_active','created_at')
    list_filter = ('is_active','categories','created_at')
    search_fields = ('name','content','short_description')
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ('tags','categories')
    ordering = ('-created_at',)

    def get_categories(self, obj):
        return " ,".join([c.title for c in obj.categories.all()])
    get_categories.short_description = 'دسته بندی ها'

@admin.register(InstagramGallery)
class InstagramGalleryAdmin(admin.ModelAdmin):
    list_display = ('id','image_preview')

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.image.url)
        return "بدون تصویر"

    image_preview.short_description = 'پیش‌نمایش'
















