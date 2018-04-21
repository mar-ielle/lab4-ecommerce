from rest_framework import serializers
from .models import User, Product, Cart

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'

		