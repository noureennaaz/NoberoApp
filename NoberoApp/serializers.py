from rest_framework import serializers

class MyModelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
# serializers.py
from rest_framework import serializers
from .models import Product, ProductSKU

class ProductSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSKU
        fields = ['color', 'sizes']

class ProductSerializer(serializers.ModelSerializer):
    available_skus = ProductSKUSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
