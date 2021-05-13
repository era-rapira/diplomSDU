from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView


from .serializers import Categor1Seriazer,ProductSerizer
from ..models import Category, Product


class CategoryAPI(ListAPIView):
    serializer_class = Categor1Seriazer
    queryset = Category.objects.all()

#filter by smartphones
class SmartphonesAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.filter(category=3)

#filter by television
class TelevisionAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.filter(category=1)

#filter by Laptops
class LaptopsAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.filter(category=2)



class ProductListAPI(ListAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.all()
    #поиск по цене и названию по
    filter_backends = [SearchFilter]
    search_fields = ['price_of_product','title_of_product']

#information about one object by id
class ProductDetailAPI(RetrieveAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.all()

#allowing to create or update or delete from product model stuff
class ProductCreateUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.all()

