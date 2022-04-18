from django.db import models
from django.urls import reverse

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200, help_text='Brand name')
    def __str__(self):
        return self.name
class ProductType(models.Model):
    name = models.CharField(max_length=200, help_text='Product type')
    def __str__(self):
        return self.name
class DisplayType(models.Model):
    name = models.CharField(max_length=200, help_text='Display type')
    def __str__(self):
        return self.name
class OS(models.Model):
    name = models.CharField(max_length=200, help_text='OS')
    def __str__(self):
        return self.name
class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    productType = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
    displayType = models.ForeignKey('DisplayType', on_delete=models.SET_NULL, null=True)
    displaySize = models.IntegerField()
    operatingSystem = models.ForeignKey('OS', on_delete=models.SET_NULL, null=True)
    deliveryTime = models.DurationField()
    deliveryCharge = models.BooleanField()
    price = models.IntegerField()
    def __str__(self):
        return f'{self.displaySize}" {self.brand} {self.displayType} {self.productType}'
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])