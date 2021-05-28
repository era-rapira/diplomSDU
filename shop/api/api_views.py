from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from .serializers import UserSeriazer
from .serializers import Categor1Seriazer,ProductSerizer,LoginSerializer,UserSeriazer
from ..models import Category, Product
from django.conf import  settings
from django.contrib import auth
import jwt
from rest_framework.generics import ListAPIView,\
    RetrieveAPIView, \
    ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView


class RegisterAPI(GenericAPIView):
    serializer_class = UserSeriazer
    def post(self,request):
        serializer = UserSeriazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSeriazer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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

class ProductCreateAPI(ListCreateAPIView):
    serializer_class = ProductSerizer
    queryset = Product.objects.all()


