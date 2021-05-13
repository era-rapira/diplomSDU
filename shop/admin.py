




from django.contrib import admin
from django import forms

from .models import *




admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Product)

admin.site.register(Customer)

