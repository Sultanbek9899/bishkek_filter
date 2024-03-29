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
    list_display = ['name', 'category', 'sub_category', 'price', 'sale_status', 'created']
    list_filter = ['category', 'price', 'sub_category', 'created', 'sale_status']
    search_fields = ['name', 'price']
    prepopulated_fields = {'slug': ('name',)}
