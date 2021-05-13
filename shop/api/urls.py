from django.urls import path

from .api_views import ProductListAPI,ProductDetailAPI,CategoryAPI,SmartphonesAPI,LaptopsAPI,TelevisionAPI,ProductCreateUpdateDeleteAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name = 'products'),
    path('categories/', CategoryAPI.as_view(), name='categories'),
    path('smartphones/', SmartphonesAPI.as_view(), name='smartphones'),
    path('laptops/', LaptopsAPI.as_view(), name='laptops'),
    path('television/', TelevisionAPI.as_view(), name='television'),
    path('product/<str:pk>', ProductDetailAPI.as_view(), name='product'),
    path('productcrud/<str:pk>', ProductCreateUpdateDeleteAPI.as_view(), name='productcrud'),

    #path('/', .as_view(), name=''),
]