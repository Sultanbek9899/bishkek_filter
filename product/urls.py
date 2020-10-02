from django.urls import path, include
from .views import *

urlpatterns = [
    path('', product_list, 'product_list'),
    path('<slug:category_slug>/', product_list, name='category_list'),
    path('<slug:category_slug>/<slug:sub_category_slug>/', product_list, name='sub_category_list')
]
