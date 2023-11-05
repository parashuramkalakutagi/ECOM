from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from accounts.serializer import ProfileSerializer


class MobileSerializer(ModelSerializer):
    class Meta:
        model = Mobiles
        fields = '__all__'

class LaptopSerializer(ModelSerializer):
    class Meta:
        model = Laptops
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Catagory
        exclude = ['created_at','updated_at']


class ProductSerializer(ModelSerializer):
    catagory = CategorySerializer(many=False)
    categorys = serializers.SerializerMethodField('get_category')
    users = serializers.SerializerMethodField('get_user')

    class Meta:
        model = item
        fields = [
            'uuid',
            'users',
            'title',
            'price',
            'product_image',
            'discount_price',
            'description',
            'currency',
            'categorys',
            'catagory',
        ]

    def get_category(self,obj):
        if obj:
            return obj.catagory.catagory_name
        else:
            return None

    def get_user(self,obj):
        if obj:
            return obj.user.first_name
        else:
            return None


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'