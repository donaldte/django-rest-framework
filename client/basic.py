import requests 


"""
endpoint: c'est l'adresse du serveur (http://httpbin.org)
en francais endpoint signifie point de terminaison
"""

endpoint = "http://localhost:8000"

# on fait une requete GET sur l'endpoint
response = requests.get(endpoint, data={"name": "John", "age": 30})

print(response.text)
print(response.status_code)

{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-67027e1b-1e41fb814d9f288614865cb7'}, 'json': None, 'method': 'GET', 'origin': '129.0.80.240', 'url': 'http://httpbin.org/anything'}