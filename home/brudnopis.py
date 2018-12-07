import json
with open('table.json', 'rt') as my_file:
    print(json.load(my_file))