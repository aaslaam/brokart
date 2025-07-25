from django.shortcuts import render

def show_login(request):
    return render(request, 'account.html')