from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sub_category', 'price', 'created']
    list_filter = ['category', 'price', 'sub_category', 'created']
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'old_price', 'new_price', 'sale_percent']
    list_filter = ['new_price', 'old_price']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}