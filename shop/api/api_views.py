from rest_framework.generics import ListAPIView

from .serializers import Categor1Seriazer, TelephonesSerializer, ProductSerizer, LaptopSerializer, TelevisionSerializer
from ..models import Category, Smartphone, Laptop, Television


class CategoryAPI(ListAPIView):
    serializer_class = Categor1Seriazer
    queryset = Category.objects.all()



class TelephoneAPI(ListAPIView):
    serializer_class = TelephonesSerializer
    queryset = Smartphone.objects.all()


class LaptopAPI(ListAPIView):
    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()



class TelevisionAPI(ListAPIView):
    serializer_class = TelevisionSerializer
    queryset = Television.objects.all()
