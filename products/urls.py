from django.contrib import admin
from django.urls import path

import products.views as products

urlpatterns = [

    path('', products.product_list_view),

]