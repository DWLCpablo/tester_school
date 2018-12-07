"""11. Write a Python program to multiply all the items in a dictionary."""

sample = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

def multiply_dic_values(dic):
    sum = 1
    for i in dic:
        sum *= dic[i]
    return sum

print(multiply_dic_values(sample))

def multiply_key_values(dic):
    sum = 1
    for i in dic:
        sum *= i
    return sum
print(multiply_key_values(sample))

if 3 in sample:
    del sample[3]
print(sample)