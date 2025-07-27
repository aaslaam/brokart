from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')


#view list products
def product_list(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request,'product.html',context)


def product_detail(request):
    return render(request, 'product_detail.html')