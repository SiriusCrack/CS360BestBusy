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
        results = Product.objects
        return render(
            request, 
            'catalog/exact_match.html', 
            {
                'search':search,
                'results':results
            }
        )
    else:
        return render(request, 'catalog/priority_criteria.html')

def serviceRequirements(request):
    if request.method == "POST":
        results = Product.objects
        hasResults = False
        minDisplaySize = request.POST['minDisplaySize']
        maxDisplaySize = request.POST['maxDisplaySize']
        deliveryTime = request.POST['deliveryTime']
        deliveryCharge = request.POST['deliveryCharge']
        price = request.POST['price']
        brand_id = request.POST['brand_id']
        displayType_id = request.POST['displayType_id']
        productType_id = request.POST['productType_id']
        if minDisplaySize and (minDisplaySize != 0):
            results = results.filter(displaySize__gte=minDisplaySize)
            hasResults = True
        if maxDisplaySize and (maxDisplaySize != 0):
            results = results.filter(displaySize__lte=maxDisplaySize)
            hasResults = True
        if deliveryTime and (deliveryTime != 0):
            results = results.filter(deliveryTime__lte=deliveryTime)
            hasResults = True
        if deliveryCharge and (deliveryCharge != 'none'):
            if deliveryCharge == 'no':
                results = results.filter(deliveryCharge=False)
                hasResults = True
        if price and (price != 0):
            results = results.filter(price__lte=price)
            hasResults = True
        if brand_id and (brand_id != '0'):
            results = results.filter(brand_id=brand_id)
            hasResults = True
        if displayType_id and (displayType_id != '0'):
            results = results.filter(displayType_id=displayType_id)
            hasResults = True
        if productType_id and (productType_id != '0'):
            results = results.filter(productType_id=productType_id)
            hasResults = True
        if hasResults:
            return render(
                request,
                'catalog/service_requirements.html',
                {
                    'results':results,
                    'hasResults':hasResults
                }
            )
        else:
            return render(request, 'catalog/service_requirements.html', {'hasResults':hasResults})
    else:
        return render(request, 'catalog/service_requirements.html')

from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'catalog/product_list.html'
class ProductDetailView(generic.DetailView):
    model = Product
    pk = Product.productID
    template_name = 'catalog/product_detail.html'