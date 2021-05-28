from rest_framework import serializers
from django.contrib.auth.models import User
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

class UserSeriazer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=123,min_length=5, write_only=True)
    email = serializers.EmailField(max_length=123, min_length=5)
    first_name = serializers.CharField(max_length=23, min_length=2)
    last_name = serializers.CharField(max_length=23,min_length=2)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']
    def validate(self, attrs):
        email =attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email',('Email is already in use')})
        return super().validate(attrs)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']

