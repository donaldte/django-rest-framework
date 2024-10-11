from rest_framework import serializers
from .models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'discount', 'amount']
        
        
    def get_discount(self, obj):
        return obj.get_discount()
    
    
    def get_amount(self, obj):
        return obj.get_price()
    
        
               