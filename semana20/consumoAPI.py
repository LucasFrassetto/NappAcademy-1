import requests

'''
| GET|HEAD  | api/dogs            | dogs.index
| POST      | api/dogs            | dogs.store
| GET|HEAD  | api/dogs/{dog}      | dogs.show
| PUT|PATCH | api/dogs/{dog}      | dogs.update
| DELETE    | api/dogs/{dog}      | dogs.destroy
'''
# GET
url = 'http://127.0.0.1:8000/api/dogs'
r = requests.get(url)
lista_cachorros = r.json()
# POST
url = 'http://127.0.0.1:8000/api/dogs'
dados = {'name': 'Super Cão', 'family': 'vira-lara'}
cadastro_novo = requests.post(url, data=dados)
print(cadastro_novo.text)
# GET
url = 'http://127.0.0.1:8000/api/dogs/3'
r = requests.get(url)
cachorro = r.json()
# PUT
url = 'http://127.0.0.1:8000/api/dogs/3'
dados = {'name': 'K-9', 'family': 'dálmata'}
r = requests.put(url, data=dados)
r.status_code
# DELETE
url = 'http://127.0.0.1:8000/api/dogs/3'
r = requests.delete(url)
