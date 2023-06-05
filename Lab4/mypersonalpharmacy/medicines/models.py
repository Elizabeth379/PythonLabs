from django.db import models

# Create your models here.
class Medicines(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%n/%d/")

    is_available = models.BooleanField(default=True)
