from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
User = get_user_model()

#Category

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name_of_category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

#Stuff
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    title_of_product = models.CharField(max_length=225,verbose_name="Title",null=True)
    slug = models.SlugField(unique=True)
    weight = models.CharField(max_length=89, verbose_name="Weight", null=True)
    image_of_product = models.ImageField(verbose_name="Image", null=True)
    description_of_product = models.TextField(verbose_name = "Descripwtion",blank=True)
    price_of_product = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Price", null=True,blank=True)
    resolution = models.CharField(max_length=215, verbose_name="Resolution",blank=True)
    accumulator_volume = models.CharField(max_length=235, verbose_name='Volume of acc',blank=True)
    random_access_memory = models.CharField(max_length=255, verbose_name="RAM", blank=True)
    videocard = models.CharField(max_length=255, verbose_name="Videocard", blank=True)
    back_camera_mp = models.CharField(max_length=255,verbose_name='Back camera',blank=True)
    front_camera_mp = models.CharField(max_length=255,verbose_name='Front camera',blank=True)
    Product_create_company = models.CharField(max_length=12,
                                              verbose_name='Which_company_produce(Hp,lenovo e.t.c)',
                                              blank=True)

    smart_technology_support = models.CharField(max_length=20, verbose_name="Smart_technologies",null=True,blank=True)


    def __str__(self):
        return self.title_of_product





class Basket(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Customer", on_delete=models.CASCADE)
    cart = models.ForeignKey('BasketItems', verbose_name="BasketItems", on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default = 1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена")







class BasketItems(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(Basket, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='total_price')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User,verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='phone number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)




