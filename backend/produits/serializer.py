from rest_framework import serializers
from .models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(max_length=255)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'discount', 'amount']
        
        
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
    
    def get_amount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_price()
    
    # validation sur le name 
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Le nom doit avoir au moins 3 caractères')
        return value
    
    
    
    
        


class PanierProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'discount', 'amount']
        
        
    def get_discount(self, obj):
        return obj.get_discount()
    
    
    def get_amount(self, obj):
        return obj.get_price()
                   