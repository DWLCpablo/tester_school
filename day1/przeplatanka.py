list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
new_list = []
for item in range(len(list1):
    new_list.append(list1[i])
    new_list.append(list2[i])
print(new_list)

result2=[]
for i, value in enumarate(list1):
    result2.append(value)
    result2.append(list2[i])
print(result2)

result3 = []
for first, second in zip(list1, list2):
    result3.append(first)
    result3.append(second)
print(result3)