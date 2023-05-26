from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking
from decimal import Decimal


class MenuSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'price_after_tax', 'menu_item_description']

    def calculate_tax(self, product:Menu):
        return product.price * Decimal(1.1)
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


