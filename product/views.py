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
        products = Product.objects.filter(availability_status=True)
    sale_products = SaleProduct.objects.all()[:6]  # для слайдера делим на два
    sale_products2 = SaleProduct.objects.all()[6:] # для второй страницы слайдера
    sale_percent = SalePicture.objects.all()[:1]

    context = {
        'products': products,
        'sale_products': sale_products,
        'sale_products2': sale_products2,
        'sale_percent_picture': sale_percent
    }

    return render(request, 'product_list.html', context=context)


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def garanty(request):
    return render(request, 'garanty.html')


def installment(request):
    return render(request, 'installment.html')


def wholesalers(request):
    return render(request, 'wholesalers.html')