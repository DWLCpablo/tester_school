example = {'a': 1, 'b': 2, 'c': 3}
print(example['a'])
#print(example['d']) #error, nie ma 'd'
print(example.get('d', None))
for i, j in example.items():
    print(i, j)

pesel = '85021312554'
print(pesel[0:2])

