from django.urls import path, include
from .views import list_product

urlpatterns = [
    path('', list_product, name="list_product")
]
