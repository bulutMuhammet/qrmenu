from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

# Register your models here.
from home.models import Category, Product, SortableBook


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['my_order']
    list_display = ['title', 'created_date', 'my_order']
    class Meta:
        model=Category

@admin.register(Product)
class ProductAdmin(SortableAdminMixin,admin.ModelAdmin):
    ordering = ['my_order']

    list_display = ['category',"title","created_date", "my_order"]
    class Meta:
        model=Product


from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin


from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin


