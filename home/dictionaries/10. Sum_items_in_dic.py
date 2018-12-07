"""10. Write a Python program to sum all the items in a dictionary. Go to the editor
"""

sample = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

def sum_dic_values(dic):
    sum = 0
    for i in dic:
        sum += dic[i]
    return sum

print(sum_dic_values(sample))

def sum_dic_keys(dic):
    sum = 0
    for i in dic:
        sum += i
    return sum

print(sum_dic_keys(sample))

print(sample.values())  # dic.values() zwraca wartości w słowniku, wewnątrz listy, więc można po nich iterować, albo zrobić sum()
print(sum(sample.values()))