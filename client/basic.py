import requests 


"""
endpoint: c'est l'adresse du serveur (http://httpbin.org)
en francais endpoint signifie point de terminaison
"""

endpoint = "http://localhost:8000/api/v1/product/detail/"

# on fait une requete GET sur l'endpoint
response = requests.get(endpoint, params={'name':'donald'}, json={'name':'donald', 'age':23, 'message':'test'})
print(response.headers)

print(response.json())
print(response.status_code)

