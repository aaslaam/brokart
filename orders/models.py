from django.db import models

from customer.models import Customer
from products.models import Product


# Oders model
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES=((DELETE, 'Delete'),
                    (LIVE, 'Live'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = (
        (ORDER_CONFIRMED, 'Order Confirmed'),
        (ORDER_PROCESSED, 'Order Processed'),
        (ORDER_DELIVERED, 'Order Delivered'),
        (ORDER_REJECTED, 'Order Rejected'),
    )

    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='added_carts')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')

    def __str__(self):
        return f"{self.product.name} in {self.owner.owner.username}'s cart"

