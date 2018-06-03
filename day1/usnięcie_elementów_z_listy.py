# napisać program który usunie z listy wszystkie wystąpienia ustlaonego elementu

lst = [2, 2, 2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
new = []
for i in lst:
    if i == 2:
        del lst[i]
    else:
        new.append(i)
print(new)


#boss
target = 10
lst1 = [10, 1, 2, 3, 10]

count = 0
for idx, value in enumerate(lst1):
    if value == target:
        count +=1

for i in range(count):
    lst1.remove(target)

print(lst1)

#v2 boss
target = 10
lst1 = [10, 1, 2, 3, 10]

count = 0
to_delete =[]

for idx, value in enumerate(lst1):
    if value == target:
        to_delete.append(idx)
for i in reversed(to_delete):
    del lst1[i]



print(lst1)
