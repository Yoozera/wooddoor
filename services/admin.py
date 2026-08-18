from django.contrib import admin

from products.models import Product
from .models import Service, ServiceCategory, ServiceStep


@admin.register(ServiceCategory)

class  ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name',)

class ServiceStepInline(admin.TabularInline):
    model = ServiceStep
    extra = 1
    fields = ('order','title','text','image')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','display_category','is_active','created_at')
    list_filter = ('is_active',)
    search_fields = ('name','short_description','description')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug':('name',)}
    inlines = [ServiceStepInline]

    def display_category(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])

    display_category.short_description = 'دسته بندی ها'

class ServiceStepAdmin(admin.ModelAdmin):
    list_display = ('title','text','order')