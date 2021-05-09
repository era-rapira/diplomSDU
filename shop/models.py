from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
User = get_user_model()

#Category

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name_of_category')
    slug = models.SlugField(unique=True)



#Stuff
class Product(models.Model):
    class Meta:
        abstract = True
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    title_of_product = models.CharField(max_length=225,verbose_name="Title")
    slug = models.SlugField(unique=True)
    image_of_product = models.ImageField(verbose_name="Image")
    description_of_product = models.TextField(verbose_name = "Descripwtion", null = True)
    price_of_product = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Pric111e")

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name="Корзина", on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    qty = models.PositiveIntegerField(default = 1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена")


    def __str__(self):
        return  "Продукт {} (для корзины)".format(self.product.title)



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






def __str__(self):
    return "Характеристики для товара {}".format(self.name)

# Now my class Product is a abstract class, so for each type of product (Smartphones, laptops i will create separate class )
class Laptop(Product):
    resolution = models.CharField(max_length=255, verbose_name="Resolution")
    display_type = models.CharField(max_length=255, verbose_name= "Display_type")
    processor_frequency = models.CharField(max_length=255, verbose_name="Frequency_of_core ")
    ram = models.CharField(max_length=12, verbose_name="RAM")
    video = models.CharField(max_length=32, verbose_name="Videocard")
    time_without_charge = models.CharField(max_length=12, verbose_name='Time_of_acc_work')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Smartphone(Product):
    resolution = models.CharField(max_length=215, verbose_name="Resolution")
    display_type = models.CharField(max_length=225, verbose_name= "Display_type")
    accumulator_volume = models.CharField(max_length=235, verbose_name='Volume of acc')
    random_access_memory = models.CharField(max_length=255, verbose_name="RAM")
    videocard = models.CharField(max_length=255, verbose_name="Videocard")
    back_camera_mp = models.CharField(max_length=255,verbose_name='Back_camera')
    front_camera_mp = models.CharField(max_length=255,verbose_name='Front_camera')

class Television(Product):
    screen_diagonal = models.CharField(max_length=12, verbose_name="screen_diagonal")
    screen_resolution = models.CharField(max_length=123, verbose_name="Resolution")

    smart_technology_support = models.CharField(max_length=20, verbose_name="Smart_technologies")

