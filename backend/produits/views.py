from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer


# Create your views here.
@api_view(['POST', 'GET'])
def product_api_view(request):
    product1 = Product.objects.all().order_by('?').first()
    data = {}
    if request.method == 'GET':
        if product1:
        
            data = ProductSerializer(product1).data 
            
    if request.method == 'POST':
        data = request.data
        print('post data', data)
        serializer = ProductSerializer(data=data)
        # form = ProductForm(data) if form.is_valid() else None
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            data = serializer.data
        # else:
        #     data = serializer.errors
       
    return Response(data)