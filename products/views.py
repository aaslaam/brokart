from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')


#view list products
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'product.html',context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})