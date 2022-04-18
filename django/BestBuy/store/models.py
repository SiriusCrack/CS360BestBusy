from django.db import models
from django.urls import reverse

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=200, help_text='Brand name')
    def __str__(self):
        return self.name
class ProductTypes(models.Model):
    name = models.CharField(max_length=200, help_text='Product type')
    def __str__(self):
        return self.name
class DisplayTypes(models.Model):
    name = models.CharField(max_length=200, help_text='Display type')
    def __str__(self):
        return self.name
class OSes(models.Model):
    name = models.CharField(max_length=200, help_text='OS')
    def __str__(self):
        return self.name
class Product(models.Model):
    brand = models.ForeignKey('Brands', on_delete=models.SET_NULL, null=True)
    productType = models.ForeignKey('ProductTypes', on_delete=models.SET_NULL, null=True)
    displayType = models.ForeignKey('DisplayTypes', on_delete=models.SET_NULL, null=True)
    operatingSystem = models.ForeignKey('OSes', on_delete=models.SET_NULL, null=True)
    deliveryTime = models.DurationField()
    deliveryCharge = models.BooleanField()
    price = models.IntegerField()
    def __str__(self):
        """String for representing the Model object."""
        return self.id
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])