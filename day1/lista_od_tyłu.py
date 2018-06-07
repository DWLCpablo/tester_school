lista = [1, 3, 'foo', 4]

for i in range(len(lista)-1, -1, -1):
    print(lista[i])


for value in reversed(lista):
    print(value)

for idx, value in enumerate(lista):
    print(idx, value)

for idx, value in enumerate(reversed(lista)):
    print(idx, value)

for pair in enumerate(lista):
    print(pair)