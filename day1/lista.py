numbers = [1, 4, -3, 0]
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for i in range(len(numbers)): #wyciąganie wartości list
    print(numbers[i])

print()
print()

for i in range(len(numbers)): #wyciąganie indeksów list
    print(i)

print()
print()

for idx, value in enumerate(numbers): #wyciąganie indeksów i wartości
    print(idx, value)


for idx, value in enumerate(numbers): #można ustawiać kolejność, i duplikować rezultaty
    print(value, idx, value)

for i in range(len(numbers)-1, -1, -1): #pobieranie wartości listy od tyłu (range ma 3 pola: 1sze to start-inclusive określony przez długość listy -1, drugi stop jeśli ma być do końca musi być na -1, trzeci step -1 = od tyłu do przodu)
    print(numbers[i], end=', ')

for value in reversed(numbers):   #odwrócona lista
    print(value)

for pair in enumerate(reversed(numbers)): #odwrócona lista, wypisanie indeksów i wartości
    print(pair)

result = []
for i, j in zip(list1, list2): # zip(lista1, lista2) łączy wspólne elementy 2 list do 1 listy docelowej, wycinając pojedynczo występujące wartości
    result.append(i)
    result.append(j)
print(result)

for i, j in zip(list1, list2): # zip(lista1, lista2) łączy wspólne elementy 2 list do 1 listy docelowej, wycinając pojedynczo występujące wartości
    result.append(i)
    result.append(j)
print(result)