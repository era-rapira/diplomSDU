from django.urls import path

from .api_views import ProductListAPI,CategoryAPI,SmartphonesAPI,LaptopsAPI,TelevisionAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name = 'products'),
    path('categories/', CategoryAPI.as_view(), name='categories'),
    path('smartphones/', SmartphonesAPI.as_view(), name='smartphones'),
    path('laptops/', LaptopsAPI.as_view(), name='laptops'),
    path('television/', TelevisionAPI.as_view(), name='television'),

    #path('/', .as_view(), name=''),
]