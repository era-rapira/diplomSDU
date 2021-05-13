from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .serializers import Categor1Seriazer,ProductSerizer
from ..models import Category, Product


class CategoryAPI(ListAPIView):
    serializer_class = Categor1Seriazer
    queryset = Category.objects.all()


class SmartphonesAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.filter(category=1)



class ProductListAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price_of_product','title_of_product']