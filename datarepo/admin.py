from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'product_quantity', 'product_category', 'date_time']
    search_fields = ['product_category', 'product_name']
    list_filter = ['product_category', 'product_name']
    ordering = ['date_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'product_name', 'price', 'quantity', 'created']
    search_fields = ['category']
    list_filter = ['category', 'product_name']
    ordering = ['created']



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)