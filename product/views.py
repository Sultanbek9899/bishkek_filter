from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def product_list(request, category_slug=None, sub_category_slug=None):

    if sub_category_slug:
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        products = Product.objects.filter(availability_status=True, sub_category=sub_category)
    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(availability_status=True, category=category)
    else:
        products = Product.objects.all(availability_status=True)

    context = {
        'products' : products

    }

    return render(request, 'product_list.html', context=context)

