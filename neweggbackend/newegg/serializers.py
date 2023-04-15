from rest_framework import serializers
from .models import Product, ShoppingCart, OrderDetails, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
  
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'])
        
        user.save()
        return user



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'product_description', 'image_url')


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
    product_name = serializers.ReadOnlyField(source='product.product_name')
    product_description = serializers.ReadOnlyField(source='product.product_description')
    
    class Meta:
        model = ShoppingCart
        fields = ('id', 'user', 'user_id', 'product', 'product_id', 'product_name', 'product_description', 'price')


class OrderDetailsSerializer(serializers.ModelSerializer):

     product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )
     user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )
     shopping_cart_id = serializers.PrimaryKeyRelatedField(
         queryset=ShoppingCart.objects.all(),
         source='shopping_cart'
     )
     class Meta:
        model = OrderDetails
        fields = ['product', 'product_id', 'user', 'user_id', 'shopping_cart_id', 'order_total']