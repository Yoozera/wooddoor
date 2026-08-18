from django.contrib import admin

from django.contrib import admin
from django.utils.html import format_html
from .models import SliderItem, ProcessStep


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    ordering = ('order',)
    fieldsets = (
        ('محتوای اصلی', {
            'fields': ('title', 'subtitle', 'image')
        }),
        ('دکمه', {
            'fields': ('button_text', 'button_link'),
        }),
        ('تنظیمات نمایش', {
            'fields': ('order', 'is_active'),
        }),
    )
    readonly_fields = ('image_preview',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 50px; width: 90px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "—"
    image_thumbnail.short_description = "تصویر"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 150px; border-radius: 6px;" />',
                obj.image.url
            )
        return "بدون تصویر"
    image_preview.short_description = "پیش‌نمایش"


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    ordering = ('order',)
    fields = ('title', 'text', 'icon_class', 'order')

    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html('<span class="{}" style="font-size: 20px;"></span> ({})', obj.icon_class, obj.icon_class)
        return "—"
    icon_preview.short_description = "آیکون"
