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
    # if request.method == 'GET':
    #     return Response({'error': 'methode get non accepte', 'status': 405})
    if product1:
        # data = {
        #     'name': product1.name,
        #     'price': product1.price,
        #     'description': product1.description,
        # }
        # data = model_to_dict(product1, fields=['id', 'name'])
        data = ProductSerializer(product1).data 
        # serialization : definition: serialization est le processus de 
        # conversion d'une instance en un format qui peut etre stocke ou transmis
        # et reconstruit plus tard
        # deserialization: definition: deserialization est le processus de 
        # conversion d'un format stocke ou transmis en une instance(ou objet)
        # prend une instance 
        # convertir cette instance en dict 
        # puis renvoie le 
    return Response(data)