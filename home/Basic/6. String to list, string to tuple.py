""" Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""

sample = 3, 5, 7, 23
lst = []
tup = ()
for item in sample:
    lst.append(str(item))
print(lst)
print(tuple(lst))

