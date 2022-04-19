from django.shortcuts import render

# Create your views here.
from .models import Brand, ProductType, DisplayType, Product

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_prods = Product.objects.all().count()

    context = {
        'num_prods': num_prods,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)