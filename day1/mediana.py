
x = 3
y = 2
z = 1

if x <= y <= z or z <= y <= x:
    print('Mediana to y i wynosi:', y)
elif z <= x <= y or y <= x <= z:
    print('Mediana to x i wynosi', x)
else:
    print('Mediana to z i wynosi', z)