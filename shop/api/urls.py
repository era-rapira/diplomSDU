from django.urls import path

from .api_views import CategoryAPI, TelephoneAPI, LaptopAPI,TelevisionAPI

urlpatterns = [
    path('categories/', CategoryAPI.as_view(), name = 'categories'),
    path('smartphones/', TelephoneAPI.as_view(), name = 'smartphones'),
    path('laptops/', LaptopAPI.as_view(), name = 'laptops'),
    path('tv/', TelevisionAPI.as_view(), name = 'television')


]