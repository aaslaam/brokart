from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='banner/')
    caption = models.CharField(max_length=255)