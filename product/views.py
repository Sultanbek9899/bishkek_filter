from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import ListCartAddProductForm


def product_list(request, category_slug=None, sub_category_slug=None):
    """Вывод список товаров"""
    if sub_category_slug:
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        products = Product.objects.filter(sale_status=False,
                                          availability_status=True,
                                          sub_category=sub_category)
    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(sale_status=False,
                                          availability_status=True, category=category)
    else:
        products = Product.objects.filter(sale_status=False, availability_status=True)
        #берем товары со скидкой
    sale_products = Product.objects.filter(sale_status=True, availability_status=True)
    sale_percent = SalePicture.objects.all()[:1]
    cart_product_form = ListCartAddProductForm()
    context = {
        'sale_products':sale_products[0:6],
        'sale_products2':sale_products[6:13],
        'products': products,
        'sale_percent_picture': sale_percent,
        'cart_product_form': cart_product_form
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