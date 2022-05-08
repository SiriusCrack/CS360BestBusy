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

def priorityCriteria(request):
    return render(request, 'catalog/priority_criteria.html')

def serviceRequirements(request):
    if request.method == "POST":
        results = Product.objects
        displaySize = request.POST['displaySize']
        deliveryTime = request.POST['deliveryTime']
        deliveryCharge = request.POST['deliveryCharge']
        price = request.POST['price']
        brand_id = request.POST['brand_id']
        displayType_id = request.POST['displayType_id']
        productType_id = request.POST['productType_id']
        if displaySize:
            results.filter(displaySize=displaySize)
        if deliveryTime:
            results.filter(displaySize=deliveryTime)
        if deliveryCharge:
            results.filter(displaySize=deliveryCharge)
        if price:
            results.filter(displaySize=price)
        if brand_id:
            results.filter(displaySize=brand_id)
        if displayType_id:
            results.filter(displaySize=displayType_id)
        if productType_id:
            results.filter(displaySize=productType_id)
        return render(
            request,
            'catalog/service_requirements.html',
            {
                'displaySize':displaySize,
                'deliveryTime':deliveryTime,
                'deliveryCharge':deliveryCharge,
                'price':price,
                'brand_id':brand_id,
                'displayType_id':displayType_id,
                'productType_id':productType_id,
                'results':results
            }
        )
    else:
        # search page
        return render(request, 'catalog/service_requirements.html')

from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/product_list.html'