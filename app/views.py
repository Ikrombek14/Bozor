from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def get_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)



def get_product_detail(request, id):
    product = Product.objects.filter(id=id)
    context = {
        'product': product
    }
    return render(request, 'products.html', context)
