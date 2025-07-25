from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'delete_status', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('delete_status', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('delete_status',)

