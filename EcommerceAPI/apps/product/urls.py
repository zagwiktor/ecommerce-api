from django.urls import path
from .views import category_list, category_detail, category_create, category_update, category_delete,\
    brand_list, brand_detail, brand_update, brand_create, brand_delete, \
    product_list, product_create, product_delete, product_detail, product_update


urlpatterns = [
    path('category-list/', category_list, name="category-list"),
    path('category-detail/<str:pk>', category_detail, name="category-detail"),
    path('category-create/', category_create, name="category-create"),
    path('category-update/<str:pk>', category_update, name="category-update"),
    path('category-delete/<str:pk>', category_delete, name="category-delete"),

    path('brand-list/', brand_list, name="brand-list"),
    path('brand-detail/<str:pk>', brand_detail, name="brand-detail"),
    path('brand-update/<str:pk>', brand_update, name="brand-update"),
    path('brand-create/', brand_create, name="brand-create"),
    path('brand-delete/<str:pk>', brand_delete, name="brand-delete"),

    path('product-list/', product_list, name="product-list"),
    path('product-detail/<str:pk>', product_detail, name="product-detail"),
    path('product-update/<str:pk>', product_update, name="product-update"),
    path('product-create/', product_create, name="product-create"),
    path('product-delete/<str:pk>', product_delete, name="product-delete"),
]
