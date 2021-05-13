from django.urls import path

from .api_views import ProductListAPI,CategoryAPI,SmartphonesAPI

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name = 'products'),
    path('categories/', CategoryAPI.as_view(), name='categories'),
    path('smartphones/', SmartphonesAPI.as_view(), name='categories'),
]