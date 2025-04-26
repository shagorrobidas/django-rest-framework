from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
