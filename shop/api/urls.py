from django.urls import path
from .api_views import ProductListAPI,ProductDetailAPI,CategoryAPI,\
    SmartphonesAPI,LaptopsAPI,TelevisionAPI,\
    ProductCreateUpdateDeleteAPI,ProductCreateAPI,RegisterAPI,LoginAPI

urlpatterns = [

    path('products/', ProductListAPI.as_view(), name = 'products'),
    path('categories/', CategoryAPI.as_view(), name='categories'),
    path('smartphones/', SmartphonesAPI.as_view(), name='smartphones'),
    path('laptops/', LaptopsAPI.as_view(), name='laptops'),
    path('television/', TelevisionAPI.as_view(), name='television'),
    path('product/<str:pk>', ProductDetailAPI.as_view(), name='product'),
    #че то хочешь изменить то по этой ссылке ниже можно
    path('productcrud/<str:pk>', ProductCreateUpdateDeleteAPI.as_view(), name='productcrud'),
    #че то хочешь создать то тебя сюда
    path('productcreate/', ProductCreateAPI.as_view(), name='product_create'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/',LoginAPI.as_view(), name='login'),

]