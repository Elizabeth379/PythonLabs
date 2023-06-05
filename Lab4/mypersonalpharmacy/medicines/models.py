from django.db import models


class Medicines(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%n/%d/")

    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

    def __str__(self):
        return self.title
