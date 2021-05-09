

from django.contrib import admin
from django import forms

from .models import *

class LaptopCategoryChoiceField(forms.ModelChoiceField):
    pass

class LaptopAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name == 'category':
            return LaptopCategoryChoiceField(Category,object.filter(slug='Laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Smartphone)
admin.site.register(Laptop)
admin.site.register(Customer)
