# dwa słowniki, napisz program który utworzy z nich listę której elementy są słownikami zawierającymi id, model i nazwę urządzenia
# oraz program który utworzy słownik którego kluczami są nazwy modeli a wartościami - listy nazw
device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}

devices = []
nowy = {}
#boss

for dev_id, name in device_names.items():
    model = device_models[dev_id]
    devices.append({'id': dev_id, 'name': name, 'model': model}) #można tworzyć w funkcji lst.append() słownik, dodając {} wewnątrz ()
print(devices)


model_map = {}
device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}


for dev_id, model in device_models.items():
    if model in model_map:
        model_map[model].append(device_names[dev_id])
    else:
        model_map[model] = [device_names[dev_id]]

print(model_map)


