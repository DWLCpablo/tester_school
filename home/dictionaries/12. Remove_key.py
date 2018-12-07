"""12. Write a Python program to remove a key from a dictionary. """

dic = {'a':1,'b':2,'c':3,'d':4}
print(dic)
if 'b' in dic:
    del dic['b']     #usuwając dic[key] usuwasz parę klucz-wartość
print(dic)