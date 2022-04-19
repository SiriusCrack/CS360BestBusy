from django.contrib import admin

# Register your models here.
from .models import Brand, ProductType, DisplayType, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    fields = ['name']
@admin.register(DisplayType)
class DisplayTypeAdmin(admin.ModelAdmin):
    fields = ['name']
@admin.register(Product)
class OSAdmin(admin.ModelAdmin):
    fields = [
        'brand',
        'productType',
        'displayType',
        'displaySize',
        'deliveryTime',
        'deliveryCharge',
        'price',
    ]