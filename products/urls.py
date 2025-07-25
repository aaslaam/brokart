from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('product-detail/<int:id>/', views.product_detail, name='product_detail'),


    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
