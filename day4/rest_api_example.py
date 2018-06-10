import requests
import hashlib

BASE_URL = 'http://polakow.eu:3000/people/'  #musi być / na końcu, bo inaczej nie będzie można nic dodawać

response = requests.get(BASE_URL, params={'_limit': 3, '_page': 2})
print(response.json())
print(response.text)
print(response.headers)
print(response.status_code)
print(response.headers['X-Total-Count'])
md5 = hashlib.md5('relayr'.encode('ascii'))
token = md5.hexdigest()
print(token)
headers = {'Authorization': 'Bearer ' + token}
person = {'first_name': 'Janusz', 'last_name': 'Cebularz', 'email': 'janusz_cebularz@gmail.com' , 'phone' : '+482222222222', 'ip_address': '192.168.1.1'}
response = requests.post(BASE_URL, json=person, headers=headers)
print(response.json())

url = BASE_URL + 'gOLqqi~'
print(requests.get(url).json())
print(requests.get(BASE_URL, params={'id': 'gOLqqi~'}).json())

cebularze = requests.get(BASE_URL, params={'first_name': 'Michas', 'last_name': 'Cebularz'}).json()
print(cebularze)

response = requests.get(BASE_URL, params={'email_like': '@gmail.com'})  #
print(response.json())
print('192.168.1.1'.startswith('192.168'))
print('abc'.starstwith('123'))
