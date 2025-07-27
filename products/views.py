from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')


#view list products and paginate products

def product_list(request):
    products = Product.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(products, 4)  # Show 4 products per page
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj
    }
    return render(request,'product.html',context)

#product detail view
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})