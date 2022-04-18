from django.contrib import admin

# Register your models here.
from .models import Brands, ProductTypes, DisplayTypes, OSes, Product

@admin.register(Brands)
@admin.register(ProductTypes)
@admin.register(DisplayTypes)
@admin.register(OSes)
@admin.register(Product)