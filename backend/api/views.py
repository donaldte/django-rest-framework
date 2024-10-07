import json
from django.shortcuts import render
from django.http import JsonResponse


def api_view(request):
    # request c'\est instance de la classe HttpRequest
    # print(dir(request))
    data = request.body 
    # return bytes data 
    data = json.loads(data)
    data['header'] = json.dumps(dict(request.headers))
    data['method'] = request.method
    data['path'] = request.path
    data['content_type'] = request.content_type
    data['params'] = request.GET
   
    return JsonResponse(data)

