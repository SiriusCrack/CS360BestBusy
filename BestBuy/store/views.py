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
            results.filter(deliveryTime=deliveryTime)
        if deliveryCharge:
            results.filter(deliveryCharge=deliveryCharge)
        if price:
            results.filter(price=price)
        if brand_id:
            results.filter(brand_id=brand_id)
        if displayType_id:
            results.filter(displayType_id=displayType_id)
        if productType_id:
            results.filter(productType_id=productType_id)
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
        return render(request, 'catalog/service_requirements.html')

from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/product_list.html'