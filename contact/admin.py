
from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'phone')
    readonly_fields = ('name', 'phone', 'created_at')
    list_editable = ('is_read',)
    ordering = ('is_read', '-created_at')  # پیام‌های خونده‌نشده اول نمایش داده بشن
    date_hierarchy = 'created_at'
    list_per_page = 25

    def has_add_permission(self, request):
        return False