from django.shortcuts import render

def cart_view(request):
    """
    View to render the cart page.
    """
    return render(request, 'cart.html')
