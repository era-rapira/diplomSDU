




from django.contrib import admin
from django import forms

from .models import *
'''

class LaptopCategoryChoiceField(forms.ModelChoiceField):
    pass

class LaptopAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name == 'category':
            return LaptopCategoryChoiceField(Category.objects.filter(slug='Laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

'''



admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Smartphone)
admin.site.register(Laptop)
admin.site.register(Customer)
admin.site.register(Television)
