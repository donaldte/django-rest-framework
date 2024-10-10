from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from .models import Product

# Create your views here.

def product_api_view(request):
    product1 = Product.objects.all().order_by('?').first()
    data = {}
    if product1:
        # data = {
        #     'name': product1.name,
        #     'price': product1.price,
        #     'description': product1.description,
        # }
        data = model_to_dict(product1, fields=['id', 'name'])
        # prend une instance 
        # convertir cette instance en dict 
        # puis renvoie le 
    return HttpResponse(data, headers={'Content-Type': 'application/json'})