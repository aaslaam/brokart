from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'product.html')
def product_detail(request):
    return render(request, 'product_detail.html')