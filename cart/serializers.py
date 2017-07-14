from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CartItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = ('user', 'product', 'quantity')
