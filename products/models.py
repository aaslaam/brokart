

from django.db import models

from django.db import models

# product model

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES=((DELETE, 'Delete'),
                    (LIVE, 'Live'))
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    featured_image = models.ImageField(upload_to='products/featured_images/', blank=True, null=True)
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str: 
        return self.title

