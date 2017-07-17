from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.
def product_details(request, id):
    product = get_object_or_404(Product,pk=id)
    return render(request, "product.html", {"product": product})
