from .models import Products
from .serializers import ProductsListSerializer
from .serializers import ProductsDetailSerializer
from .serializers import ProductsCreateUpdateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated


class ProductsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsListSerializer
    queryset = Products.objects.all()

class ProductsDetailAPI(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Products.objects.all()

class ProductsCreateAPI(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsCreateUpdateSerializer
    queryset = Products.objects.all()

class ProductsUpdateAPI(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsCreateUpdateSerializer
    queryset = Products.objects.all()

class ProductsDeleteAPI(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductsDetailSerializer
    queryset = Products.objects.all()