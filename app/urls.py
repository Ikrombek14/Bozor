from django.urls import path
from .views import get_category, get_product_detail

urlpatterns = [
    path("", get_category, name="get_category"),
    path("products/<int:id>", get_product_detail, name="get_product_detail")


]