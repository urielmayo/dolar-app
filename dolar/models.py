from django.db import models
from django.utils.text import slugify


# Create your models here.
class Dolar(models.Model):
    """Model definition for Dolar."""

    # TODO: Define fields here
    name = models.CharField(max_length=70)
    description = models.TextField()
    sell_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    buy_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    slug = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Dolar."""

        verbose_name = 'Dolar'
        verbose_name_plural = 'Dolars'

    def __str__(self):
        """Unicode representation of Dolar."""
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
