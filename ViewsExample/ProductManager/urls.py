from django.urls import path
from .views import product_list, product_overview

urlpatterns = [
    path('', product_list),
    path('product-overview/<int:pk>', product_overview, name="product-overview")
]
