from django.urls import path, include
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('garanty/', garanty, name='garanty'),
    path('contacts/', contacts, name='contacts'),
    path('wholesalers/', wholesalers, name='wholesalers'),
    path('installment/', installment, name='installment'),
    path('<slug:category_slug>/', product_list, name='category_list'),
    path('<slug:category_slug>/<slug:sub_category_slug>/', product_list, name='sub_category_list')
]
