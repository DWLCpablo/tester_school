numbers = [1, 4, -3, 0]
empty = []
print(numbers[2])
print(len(numbers))
numbers[2] = 10
print(numbers[2])

for i in numbers:
    print(i, end=', ')

for i in range(len(numbers)):
    print(numbers[i])