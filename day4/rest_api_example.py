import requests

BASE_URL = 'http://polakow.eu:3000/people/'  #musi być / na końcu, bo inaczej nie będzie można nic dodawać

response = requests.get(BASE_URL, params={'_limit': 3, '_page': 2})
print(response.json())
print(response.text)
print(response.headers)
print(response.status_code)
print(response.headers['X-Total-Count'])