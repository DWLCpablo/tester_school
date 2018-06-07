lista = [{'id': 1, 'model': 'AFE3'}, {'id': 2, 'model': 'FTY'}]
for item in lista:
    print(item)
    print(item['id'])
print([item for item in lista])
print([item['id'] for item in lista])