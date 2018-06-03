example = {'a': 1, 'b': 2, 'c': 3}
print(example['a'])
#print(example['d']) #error, nie ma 'd'
print(example.get('d', 5))