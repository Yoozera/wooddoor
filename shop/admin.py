from django import forms
from django.contrib import admin
from .models import ShopCategory, ShopProduct, ShopTag, ShopProductImage
from services.models import Service


class ShopProductImageInline(admin.TabularInline):
    model = ShopProductImage
    extra = 1
    can_delete = True


class ShopProductAdminForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple('خدمات', is_stacked=False),
        label='خدمات مرتبط'
    )

    class Meta:
        model = ShopProduct
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['services'].initial = self.instance.services.all()

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            instance.services.set(self.cleaned_data['services'])
        else:

            self._save_services_later = True
        return instance

    def save_m2m(self):
        super().save_m2m()
        self.instance.services.set(self.cleaned_data['services'])


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    form = ShopProductAdminForm
    list_display = ('name', 'display_category', 'get_service', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    inlines = [ShopProductImageInline]
    filter_horizontal = ('category', 'tags')

    class Media:
        css = {
            'all': ('admin/css/widgets.css',)
        }

    def display_category(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    display_category.short_description = 'دسته بندی ها'

    def get_service(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    get_service.short_description = 'سرویس های مرتبط'


@admin.register(ShopTag)
class ShopTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']