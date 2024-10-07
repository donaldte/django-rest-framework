from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Create your views here.

def product_api_view(request):
    product1 = Product.objects.all().order_by('?').first()
    data = {}
    if product1:
        data = {
            'name': product1.name,
            'price': product1.price,
            'description': product1.description,
        }
        
        # serialisation de l'objet
        """
        Definition: Serialization is the process of converting an object into a stream of bytes to store the object or transmit it to memory, a database, or a file. Its main purpose is to save the state of an object in order to be able to recreate it when needed.
        en francais: La sérialisation est le processus de conversion 
        d'un objet en un flux d'octets pour stocker l'objet ou 
        le transmettre \en mémoire, dans une base de données ou 
        dans un fichier. Son objectif principal est de sauvegarder 
        l'état d'un objet afin de pouvoir le recréer en cas de besoin.
        """
    return JsonResponse(data)