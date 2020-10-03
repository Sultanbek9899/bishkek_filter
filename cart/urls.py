from django.urls import path
from .views import *

urlpatterns=[
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', list_card_add, name='cart_add'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_update'),
    path('remove/<int:product_id>', cart_remove, name='cart_remove')
]