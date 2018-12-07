import json
# dwa słowniki, napisz program który utworzy z nich listę której elementy są słownikami zawierającymi id, model i nazwę urządzenia
# oraz program który utworzy słownik którego kluczami są nazwy modeli a wartościami - listy nazw
device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}

devices = []
nowy = {}

for key, value in device_names.items():
    model = device_models[key]
    devices.append({'id': key, 'name': value, 'model': model})  #można tworzyć w funkcji lst.append() słownik, dodając {} wewnątrz ()
print(devices)

for key, value in device_models.items():
    if value in nowy:
        nowy[value].append(device_names[key])
    else:
        nowy[value] = [device_names[key]]
print(nowy)

def to_json(data):
    return json.dumps(data)

json_nowy = to_json(nowy)
print(json_nowy)

def from_json(json_data):
    return json.loads(json_data)

print(from_json(to_json(nowy)))