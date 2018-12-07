import json
import requests
import hashlib

BASE_URL = 'http://polakow.eu:3000/people/'  #musi być / na końcu, bo inaczej nie będzie można nic dodawać

response = requests.get(BASE_URL, params={'_limit': 5})  # params={'key': value, ...}
print(response)  #zwróci kod 200
print(response.json())  #zwróci zawartość bazy danych w obiekcie json
print(response.text)  #zwróci zawarrtość jako txt

with open('people.txt', 'wt') as my_file:  # działa,
    my_file.write(response.text)

with open('people.txt', 'rt') as my_file: #działa
    lines = my_file.readlines()
    for line in lines:
        print(line)

print(response.headers)
print(response.headers['X-Total-Count'])  #headers daje w odpowiedzi słownik, można się odwoływać do kluczy i wartości w środku
for key in response.headers:
    if key == 'Cache-Control':
        print(key, response.headers[key])

print('Response:', response.status_code)
md5 = hashlib.md5('relayr'.encode('ascii'))
token = md5.hexdigest()
print('Token:', token)
head = {'Authorization': 'Bearer ' + token}
person = {'first_name': 'Jose Mourinho', 'last_name': 'The Bottom Feeder', 'email': 'scum_of_the_earth@filthyplace.com', 'phone' : '+482222222222', 'ip_address': '111.111.1.1'}
#response_post = requests.post(BASE_URL, json=person, headers=head)
#print(response_post.json())
#if response_post.status_code == 201:
#    print('Post succesful!')

#print(requests.get(BASE_URL, params={'first_name' : 'Jaime'}).json())  #działa, zapamiętaj składnię:
                                                                # requests.KOMENDA(url, params={'cos': 'coś'}).json())

#print('Wszytkich o nazwisku zaczynającym się na J')
#print(requests.get(BASE_URL, params={'last_name_like' : 'J'}).json())
response = requests.get(BASE_URL, params={'first_name' : 'Janusz'})
for item in response:
    print(item)
