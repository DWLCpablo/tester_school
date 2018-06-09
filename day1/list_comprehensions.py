dev_id = []
for i in range(1, 5):
    dev_id.append('device_' + str(i))
print(dev_id)

print(['device_' + str(i) for i in range(1, 5)]) # to samo zapisane wyrażeniem listowym / list comprehensions

print([i ** 2 for i in range(1, 101)])
print(i ** 2 for i in range(1, 101))
