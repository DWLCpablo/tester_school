import json

data = {'spam': (1, 2, 3), 'eggs' : {'a': 2, 'b': 3}}
serialized = json.dumps(data)
print(data)
print(serialized)
data2 = json.loads(serialized)
print(data2)

with open('data1.json', 'wt') as json_file:
    json.dump(data, json_file)

with open('data.json', 'rt') as json_file:
    print(json.load(json_file))

person = {'first_name': 'Jose Mourinho', 'last_name': 'The Bottom Feeder', 'email': 'scum_of_the_earth@filthyplace.com', 'phone' : '+482222222222', 'ip_address': '111.111.1.1'}
with open('jose.json', 'wt') as my_file:
    json.dump(person, my_file)

with open('jose.json', 'rt') as my_file:
    print(json.load(my_file))