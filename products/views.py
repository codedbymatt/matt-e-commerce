from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    # args = {}
    # args.update(csrf(request))
    return render(request, "categories.html", {"products": products})


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
