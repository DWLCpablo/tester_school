# moja wersja
lista = [2, 3, 4, 5, 4, 2, 3, 2, 10, 5, 5, 11]
max = 0

for item in lista:
    if item > max:
        max = item
print('maximum number in lista is', max)
#boss
for idx, value in enumerate(lista):
    if idx == 0:
        current_min = value
        current_max = value
    elif current_max < value:
        current_max = value
    elif current_min > value:
        current_min = value

print('Maximum: ', current_max)
print('Minimum: ', current_min)