from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
User = get_user_model()

#Category

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя катерогии')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


#Stuff
class Product(models.Model):
    class Meta:
        abstract = True
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name = "Описание", null = True)
    price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name="Корзина", on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    qty = models.PositiveIntegerField(default = 1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена")


    def __str__(self):
        return  "Продукт {} (для корзины)".format(self.product.title)



class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9,decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User,verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)






def __str__(self):
    return "Характеристики для товара {}".format(self.name)

# Now my class Product is a abstract class, so for each type of product (Smartphones, laptops i will create separate class )
class Laptop(Product):
    diagonal = models.CharField(max_length=255, verbose_name="Диагональ")
    display_type = models.CharField(max_length=255, verbose_name= "Тип дисплея")
    processor_frequency = models.CharField(max_length=255, verbose_name="Частота процессора ")
    ram = models.CharField(max_length=255, verbose_name="Оперативная память")
    video = models.CharField(max_length=255, verbose_name="Видеокарта")
    time_without_charge = models.CharField(max_length=255, verbose_name='Время работы от аккумулятора')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name="Диагональ")
    display_type = models.CharField(max_length=255, verbose_name= "Тип дисплея")
    resolution = models.CharField(max_length=255, verbose_name="Разширение")
    accumulator_volume = models.CharField(max_length=255, verbose_name='Объем аккумулятора')
    random_access_memory = models.CharField(max_length=255, verbose_name="Оперативная память")
    video = models.CharField(max_length=255, verbose_name="Видеокарта")
    back_camera_mp = models.CharField(max_length=255,verbose_name='Задняя камера')
    front_camera_mp = models.CharField(max_length=255,verbose_name='Передняя камера')

