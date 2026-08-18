from django.contrib import admin
from django.utils.html import format_html
from .models import AboutUs, FunFact, TeamMember, Testimonial,SiteBackground


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    fields = ('title', 'bold_text', 'description', 'image', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border-radius: 6px;" />',
                obj.image.url
            )
        return "بدون تصویر"
    image_preview.short_description = "پیش‌نمایش تصویر"


@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'order')
    list_editable = ('number', 'order')
    search_fields = ('title',)
    ordering = ('order',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'name', 'designation', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'designation')
    list_filter = ('designation',)
    ordering = ('order',)
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'designation', 'bio', 'image', 'order')
        }),
        ('شبکه‌های اجتماعی', {
            'fields': ('facebook', 'twitter', 'linkedin', 'pinterest'),
            'classes': ('collapse',),
        }),
    )

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 50px; width: 50px; object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return "بدون تصویر"
    image_thumbnail.short_description = "تصویر"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'designation', 'stars', 'order')
    list_editable = ('order',)
    search_fields = ('client_name', 'designation')
    list_filter = ('rating',)
    ordering = ('order',)

    def stars(self, obj):
        return format_html('⭐' * obj.rating)
    stars.short_description = "امتیاز"

@admin.register(SiteBackground)
class SiteBackgroundAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'bg_preview')
    readonly_fields = ('bg_preview',)
    fields = ('testimonial_bg', 'bg_preview')

    def bg_preview(self, obj):
        if obj.testimonial_bg:
            return format_html(
                '<img src="{}" style="max-height: 100px; border-radius: 6px;" />',
                obj.testimonial_bg.url
            )
        return "بدون تصویر"
    bg_preview.short_description = "پیش‌نمایش"

    def has_add_permission(self, request):
        # اگه یه رکورد از قبل هست، اجازه اضافه کردن رکورد جدید رو نده
        return not SiteBackground.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # اجازه حذف نده تا سایت بدون بک‌گراند نمونه
        return False