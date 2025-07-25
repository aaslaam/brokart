from django.db import models
from django.contrib.auth.models import User



# Customer model

class Customer(models.Model):
    LIVE = 1
    DELETE = 0
    STATUS_CHOICES = (
        (LIVE, 'LIVE'),
        (DELETE, 'DELETE'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user = models.ForeignKey(User, related_name='customer_profile', on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
