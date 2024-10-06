import requests 


"""
endpoint: c'est l'adresse du serveur (http://httpbin.org)
en francais endpoint signifie point de terminaison
"""

endpoint = "http://localhost:8000/api/v1/"

# on fait une requete GET sur l'endpoint
response = requests.get(endpoint)

print(response.json())
print(response.status_code)

