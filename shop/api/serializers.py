from rest_framework import serializers

from ..models import Category, Product, Smartphone, Laptop, Television


class Categor1Seriazer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
          'id', 'name', 'slug'
        ]



class ProductSerizer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title_of_product = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image_of_product = serializers.ImageField(required=True)
    description_of_product = serializers.CharField(required=True)
    price_of_product = serializers.DecimalField(max_digits=12, decimal_places=2, required=True)


class TelephonesSerializer(ProductSerizer, serializers.ModelSerializer):
    resolution = serializers.CharField(required=True)
    accumulator_volume = serializers.CharField(required=True)
    random_access_memory = serializers.CharField(required=True)
    videocard = serializers.CharField(required=False)
    back_camera_mp = serializers.CharField(required=True)
    front_camera_mp = serializers.CharField(required=True)
    Product_create_company = serializers.CharField(required=True)

    class Meta:
        model = Smartphone
        fields = '__all__'


class LaptopSerializer(ProductSerizer, serializers.ModelSerializer):
    resolution = serializers.CharField(required=True)
    processor = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    video = serializers.CharField(required=True)
    Product_create_company = serializers.CharField(required=True)

    class Meta:
        model = Laptop
        fields = '__all__'


class TelevisionSerializer(ProductSerizer, serializers.ModelSerializer):
    screen_diagonal = serializers.CharField(required=True)
    screen_resolution = serializers.CharField(required=True)
    smart_technology_support = serializers.CharField(required=True)
    company_produces = serializers.CharField(required=True)
    class Meta:
        model = Television
        fields = '__all__'

