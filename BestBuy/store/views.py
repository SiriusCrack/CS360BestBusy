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

def exactMatch(request):
    if request.method == "POST":
        search = request.POST['search']
        results = Product.objects.filter(productID=search)
        return render(
            request, 
            'catalog/exact_match.html', 
            {
                'search':search,
                'results':results
            }
        )
    else:
        return render(request, 'catalog/exact_match.html')

from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/product_list.html'

class exactMatchListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/exact_match.html'