from rest_framework import serializers

from ..models import Category, Product


class Categor1Seriazer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()


    class Meta:
        model = Category
        fields = '__all__'



class ProductSerizer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title_of_product = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    weight = serializers.CharField(required=True)
    image_of_product = serializers.ImageField(required=True)
    description_of_product = serializers.CharField(required=True)
    price_of_product = serializers.DecimalField(required=True, max_digits=12, decimal_places=0)
    resolution = serializers.CharField(required=False)
    accumulator_volume = serializers.CharField(required=False)
    random_access_memory = serializers.CharField(required=False)
    videocard = serializers.CharField(required=False)
    back_camera_mp = serializers.CharField(required=False)
    front_camera_mp = serializers.CharField(required=False)
    Product_create_company = serializers.CharField(required=False)


    class Meta:
        model = Product
        fields = '__all__'